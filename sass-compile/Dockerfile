FROM node:14-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

# -- for dev the volumes are mounted in docker-compose.yaml
# -- for prod use this as a template to build css and then use
# COPY --from=build main.css .
# -- in the wagtail dockerfile to copy the compiled css file in to the final image

CMD ["npm", "run", "css"]
