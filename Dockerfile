FROM python:3.8-alpine as build-stage
LABEL maintainer="mahdih3idari@gmail.com"

ADD . /opt/writeups/
WORKDIR /opt/writeups
RUN pip install -r requirements.txt && mkdocs build


FROM nginx:mainline-alpine
COPY --from=build-stage /opt/writeups/site /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
