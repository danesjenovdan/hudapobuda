#!/bin/bash

sudo docker login rg.fr-par.scw.cloud/djnd -u nologin -p $SCW_SECRET_TOKEN

# BUILD AND PUBLISH HUDA POBUDA
sudo docker build -f Dockerfile -t hudapobuda-staging:latest .
sudo docker tag hudapobuda-staging:latest rg.fr-par.scw.cloud/djnd/hudapobuda-staging:latest
sudo docker push rg.fr-par.scw.cloud/djnd/hudapobuda-staging:latest
