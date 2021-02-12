import pymongo

from app.core.config import settings

MongoClient = pymongo.MongoClient(
    "mongodb://{user}:{pas}@{url}".format(
        user=settings.MONGO_USERNAME,
        pas=settings.MONGO_PASSWORD,
        url=settings.MONGO_HOST,
    )
)
