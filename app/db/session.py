import pymongo
from app.core.config import settings

MongoClient = pymongo.MongoClient(
    "mongodb://{user}:{pas}@{url}".format(
        user=settings.MONGO_USER, pas=settings.MONGO_PASS, url=settings.MONGO_URL
    )
)
