import requests

from app.core.config import settings


def test_get_tx_by_hash() -> None:
    url = (
        settings.SERVER_HOST
        + "tx/hash/0xd007cf25e28a98066f27a6ea113e41c34a3deaf91a1e17456949714997f9e642"
    )

    response = requests.get(url)
    assert response.status_code == 200


def test_get_txs_latest_block() -> None:
    url = settings.SERVER_HOST + "tx/block"

    response = requests.get(url)
    assert response.status_code == 200


def test_get_txs_by_height() -> None:
    url = settings.SERVER_HOST + "tx/block/10000000"

    response = requests.get(url)
    assert response.status_code == 200
