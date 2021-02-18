# Icon Rest API

Service container to be used with [icon-api]() stack. 
This service is used to retrieve historical data from the Icon blockchain

Docker hub [image](https://hub.docker.com/r/geometrylabs/icon-rest-api)

## Endpoints
> All endpoints that return arrays have a `skip` and `limit` parameter

| Path | Description | Response Type |
|------|-------------|---------------|
| /blocks | `GET` latest blocks | array |
| /blocks/height/{height} | `GET` block by height | object |
| /blocks/hash/{hash} | `GET` block by hash | object |
| /tx/hash/{hash} | `GET` transaction by hash | object |
| /tx/address/{address} | `GET` transaction by from address | array |
| /tx/block | `GET` transactions in the latest blocks | array |
| /tx/block/{height} | `GET` transactions by block height | array |
| /events/tx/{hash} | `GET` event logs by from_address | array |
| /events/block | `GET` event logs in the latest blocks | array |
| /events/block/{height} | `GET` event logs by block height | array |


## Docker build
```
docker build . -t icon-rest-api:latest
docker run \
  -p "8000:8000" \
  -e ICON_REST_API_PORT="8000"
  -e ICON_REST_API_PREFIX="/api/v1"
  -e ICON_REST_API_MONGO_HOST="mongodb:27017"
  -e ICON_REST_API_MONGO_USERNAME="admin"
  -e ICON_REST_API_MONGO_PASSWORD="changethis"
  icon-rest-api:latest
```

## Enviroment Variables

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| ICON_REST_API_PORT | exposed port for rest api | "8000" | False |
| ICON_REST_API_PREFIX | prefix used for every endpoint | "" | False |
| ICON_REST_API_MONGO_HOST | host location of mongodb server | None | True |
| ICON_REST_API_MONGO_USERNAME | username for mongodb | None | True |
| ICON_REST_API_MONGO_PASSWORD | password for mongodb| None | True |
