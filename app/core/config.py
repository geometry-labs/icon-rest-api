from os import environ, getenv

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):

    ICON_REST_API_ENDPOINT_PREFIX: str = "/api/v1"

    MONGO_URL: str
    MONGO_USER: str
    MONGO_PASS: str

    class Config:
        case_sensitive = True


if getenv("ENV_FILE"):
    settings = Settings(_env_file=environ["ENV_FILE"])
else:
    settings = Settings()
    
