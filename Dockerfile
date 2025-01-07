FROM python:3.11-alpine AS build-stage
LABEL maintainer="mahdih3idari@gmail.com"

RUN apk add --no-cache git
WORKDIR /opt/writeups
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdocs build


FROM nginx:mainline-alpine
COPY --from=build-stage /opt/writeups/site /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
