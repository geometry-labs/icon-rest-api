import pymongo

from app.core.config import settings

MongoClient = pymongo.MongoClient(
    "mongodb://{user}:{pas}@{url}".format(
        user=settings.ICON_REST_API_MONGO_USERNAME,
        pas=settings.ICON_REST_API_MONGO_PASSWORD,
        url=settings.ICON_REST_API_MONGO_HOST,
    )
)
