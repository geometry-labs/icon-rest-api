from app.db.session import MongoClient


class CRUDTransaction:
    def get_by_hash(self, hash):
        tx = MongoClient["icon"]["transactions"].find_one(
            {"hash": {"$eq": hash}}, {"_id": 0}
        )

        return tx

    def get_by_address(self, address, skip=0, limit=0):
        tx_cursor = (
            MongoClient["icon"]["transactions"]
            .find({"from_address": {"$eq": address}}, {"_id": 0})
            .skip(skip)
            .limit(limit)
        )

        txs = []
        for t in tx_cursor:
            txs.append(t)

        return txs

    def get_by_latest_block(self, skip=0, limit=0):
        latest_block_height = MongoClient["icon"]["blocks"].find_one(
            {}, {"_id": 0, "number": 1}, sort=[("number", -1)]
        )["number"]

        tx_cursor = (
            MongoClient["icon"]["transactions"]
            .find({"block_number": {"$eq": latest_block_height}}, {"_id": 0})
            .skip(skip)
            .limit(limit)
        )

        txs = []
        for t in tx_cursor:
            txs.append(t)

        return txs

    def get_by_block(self, height, skip=0, limit=0):
        tx_cursor = (
            MongoClient["icon"]["transactions"]
            .find({"block_number": {"$eq": height}}, {"_id": 0})
            .skip(skip)
            .limit(limit)
        )

        txs = []
        for t in tx_cursor:
            txs.append(t)

        return txs


transaction = CRUDTransaction()
