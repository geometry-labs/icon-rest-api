import os

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str

    MONGO_HOST: str
    MONGO_USERNAME: str
    MONGO_PASSWORD: str

    SERVER_HOST: str

    class Config:
        case_sensitive = True


if os.environ.get("ENV_FILE", False):
    settings = Settings(_env_file=os.environ.get("ENV_FILE"))
else:
    settings = Settings()
