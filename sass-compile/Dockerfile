# ---------------------------------- WARNING ----------------------------------
# This file is primarily for development use with docker-compose
# See Dockerfile in repository root for production and k8s use
# ---------------------------------- WARNING ----------------------------------

FROM node:14-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

CMD ["npm", "run", "css"]
