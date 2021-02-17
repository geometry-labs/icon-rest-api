import os

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):

    ICON_REST_API_PORT: str = "8000"
    ICON_REST_API_PREFIX: str = ""
    ICON_REST_API_MONGO_HOST: str
    ICON_REST_API_MONGO_USERNAME: str
    ICON_REST_API_MONGO_PASSWORD: str

    class Config:
        case_sensitive = True


if os.environ.get("ENV_FILE", False):
    settings = Settings(_env_file=os.environ.get("ENV_FILE"))
else:
    settings = Settings()
