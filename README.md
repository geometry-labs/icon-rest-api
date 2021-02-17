# Icon Rest API

Service container to be used with [icon-api]() stack. 
This service is used to retrieve historical data from the Icon blockchain

Docker hub [image](https://hub.docker.com/r/geometrylabs/icon-rest-api)

## Docker build
```
docker build . -t icon-rest-api:latest
docker run \
  -p "8000:8000" \
  -e
  kafka-websocket-server:latest
```

## Enviroment Variables

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| ICON_REST_API_PORT | exposed port for rest api | "8000" | False |
| ICON_REST_API_PREFIX | prefix used for every endpoint | "" | False |
| ICON_REST_API_MONGO_HOST | host location of mongodb server | None | True |
| ICON_REST_API_MONGO_USERNAME | username for mongodb | None | True |
| ICON_REST_API_PORT | password for mongodb| None | True |
