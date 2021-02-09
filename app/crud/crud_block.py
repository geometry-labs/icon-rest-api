from app.db.session import MongoClient


class CRUDBlock:
    def get_latest_blocks(self, skip=0, limit=1):
        blocks_cursor = (
            MongoClient["icon"]["blocks"]
            .find({}, {"_id": 0}, sort=[("number", -1)])
            .skip(skip)
            .limit(limit)
        )

        blocks = []
        for b in blocks_cursor:
            blocks.append(b)

        return blocks

    def get_by_height(self, height):
        block = MongoClient["icon"]["blocks"].find_one(
            {"number": {"$eq": height}}, {"_id": 0}
        )

        return block

    def get_by_hash(self, hash):
        block = MongoClient["icon"]["blocks"].find_one(
            {"hash": {"$eq": hash}}, {"_id": 0}
        )

        return block


block = CRUDBlock()
