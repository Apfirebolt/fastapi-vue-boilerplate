

FROM node:16 as build-stage

WORKDIR /client
COPY package.json .
RUN npm install
COPY . .

RUN npm run build
