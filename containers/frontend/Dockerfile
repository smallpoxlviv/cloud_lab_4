FROM node:16-alpine AS build-step

WORKDIR /app

RUN apk --no-cache add git

RUN git clone https://github.com/smallpoxlviv/cloud_lab_4.git
WORKDIR /app/cloud_lab_4

RUN npm install
RUN npm run build

FROM nginx:stable-alpine

COPY --from=build-step /app/cloud_lab_4/build /usr/share/nginx/html

WORKDIR /defaultconf

RUN git clone https://github.com/smallpoxlviv/cloud_lab_4.git
WORKDIR /defaultconf/cloud_lab_4/containers

RUN cp /defaultconf/cloud_lab_4/containers/default.conf /etc/nginx/conf.d/default.conf

#COPY default.conf /etc/nginx/conf.d/default.conf
