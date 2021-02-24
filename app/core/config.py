import os

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):

    PORT: str = "8000"
    PREFIX: str = ""
    MONGO_HOST: str
    MONGO_USERNAME: str
    MONGO_PASSWORD: str

    class Config:
        case_sensitive = True
        env_prefix = "ICON_REST_API_"


if os.environ.get("ENV_FILE", False):
    settings = Settings(_env_file=os.environ.get("ENV_FILE"))
else:
    settings = Settings()
