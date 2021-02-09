from app.db.session import MongoClient


class CRUDEvent:
    def get_by_tx(self, hash, skip=0, limit=0):
        event_cursor = (
            MongoClient["icon"]["logs"]
            .find({"transaction_hash": {"$eq": hash}}, {"_id": 0})
            .skip(skip)
            .limit(limit)
        )

        events = []
        for e in event_cursor:
            events.append(e)

        return events

    def get_by_latest_block(self, skip=0, limit=0):
        latest_block_height = MongoClient["icon"]["blocks"].find_one(
            {}, {"_id": 0, "number": 1}, sort=[("number", -1)]
        )["number"]

        event_cursor = (
            MongoClient["icon"]["logs"]
            .find({"block_number": {"$eq": latest_block_height}}, {"_id": 0})
            .skip(skip)
            .limit(limit)
        )

        events = []
        for e in event_cursor:
            events.append(e)

        return events

    def get_by_block(self, height, skip=0, limit=0):
        event_cursor = (
            MongoClient["icon"]["logs"]
            .find({"block_number": {"$eq": height}}, {"_id": 0})
            .skip(skip)
            .limit(limit)
        )

        events = []
        for e in event_cursor:
            events.append(e)

        return events


event = CRUDEvent()
