#!/bin/bash

#################################
# set these up before you begin #
#################################
FROM_POD_NAME="hudapobuda-staging-deployment-numbersand-letters"
TO_POD_NAME="hudapobuda-deployment-numbersand-letters"
DB_PORT="5432"

echo "WARNING! If you did not update the code, don't bother running this. Update the code on production first!"
read -p "Are you sure you want to migrate? [y/N]" -n 1 -r
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "Exiting ..."
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1 # handle exits from shell or function but don't exit interactive shell
fi

#################################
# user confirmed, let's do this #
#################################
echo "Downloading FROM -> localhost"
# copy FROM to localhost
kubectl cp hudapobuda/$FROM_POD_NAME:/pvc/media ./candidate/pvc/media/
kubectl cp hudapobuda/$FROM_POD_NAME:/pvc/static ./candidate/pvc/static/
echo "Done downloading FROM -> localhost"

echo "Downloading TO -> localhost"
# backup (copy) TO to localhost
kubectl cp hudapobuda/$TO_POD_NAME:/pvc/media ./backup/pvc/media/
kubectl cp hudapobuda/$TO_POD_NAME:/pvc/static ./backup/pvc/static/
echo "Done downloading TO -> localhost"

# copy from localhost to TO
echo "Uploading FROM (localhost) -> TO"
kubectl cp ./candidate/pvc/media hudapobuda/$TO_POD_NAME:/pvc/ # beware of slashes
kubectl cp ./candidate/pvc/static hudapobuda/$TO_POD_NAME:/pvc/ # beware of slashes
echo "Done uploading FROM (localhost) -> TO"

# port-forward the db
echo "Files are copied."
echo "I will now port forward the Postgresql instance to localhost:5432."
kubectl port-forward postgresql-0 5432:$DB_PORT -n shared

# pg_dump FROM
echo "Dumping FROM, you'll have to enter the postgres password."
pg_dump --dbname=hudapobuda_staging --file=./candidate/db/FROM-dump.sql --clean --username=postgres --host=localhost --port=$DB_PORT
echo "Done dumping FROM"

# pg_dump TO
echo "Dumping TO, you'll have to enter the postgres password (again)."
pg_dump --dbname=hudapobuda --file=./backup/db/TO-dump.sql --clean --username=postgres --host=localhost --port=$DB_PORT
echo "Done dumping TO"

# one final check before we update the production database
echo "I'm about to restore - this will manipulate the production database."
read -p "Are you sure you want to do this? [y/N]" -n 1 -r
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "Exiting ..."
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1 # handle exits from shell or function but don't exit interactive shell
fi

psql --file=./candidate/db/FROM-dump.sql --username=postgres --host=localhost --port=$DB_PORT hudapobuda

echo "All done. Now go and check if it worked correctly."
