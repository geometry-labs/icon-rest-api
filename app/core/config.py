from os import environ, getenv

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str

    MONGO_URL: str
    MONGO_USER: str
    MONGO_PASS: str

    class Config:
        case_sensitive = True


if getenv("ENV_FILE"):
    settings = Settings(_env_file=environ["ENV_FILE"])
else:
    settings = Settings()
    
