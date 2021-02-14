import os

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):

    API_ENDPOINT_PREFIX: str = "/api/v1"

    MONGO_HOST: str
    MONGO_USERNAME: str
    MONGO_PASSWORD: str

    # SERVER_HOST: str

    class Config:
        env_prefix = "icon_rest_"


if os.environ.get("ENV_FILE", False):
    settings = Settings(_env_file=os.environ.get("ENV_FILE"))
else:
    settings = Settings()
