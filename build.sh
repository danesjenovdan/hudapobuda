#!/bin/bash

sudo docker login rg.fr-par.scw.cloud/djnd -u nologin -p $SCW_SECRET_TOKEN

# BUILD AND PUBLISH HUDA POBUDA
sudo docker build -f hudapobuda/Dockerfile -t hudapobuda:latest .
sudo docker tag hudapobuda:latest rg.fr-par.scw.cloud/djnd/hudapobuda:latest
sudo docker push rg.fr-par.scw.cloud/djnd/hudapobuda:latest
