import requests
from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_tx_by_hash(prep_fixtures, client: TestClient):
    r = client.get(f"{settings.ICON_REST_API_PREFIX}/tx/block")
    response = r.json()

    latest_hash = response[0]["hash"]
    latest_height = response[0]["block_number"]

    r = client.get(
        f"{settings.ICON_REST_API_PREFIX}/tx/hash/{latest_hash}"
    )
    response = r.json()
    assert r.status_code == 200
    assert response["block_number"] == latest_height


# def test_get_tx_by_hash() -> None:
#     url = (
#         settings.SERVER_HOST
#         + "tx/hash/0xd007cf25e28a98066f27a6ea113e41c34a3deaf91a1e17456949714997f9e642"
#     )
#
#     response = requests.get(url)
#     assert response.status_code == 200


def test_get_txs_latest_block(prep_fixtures, client: TestClient):
    r = client.get(f"{settings.ICON_REST_API_PREFIX}/tx/block")
    response = r.json()
    assert r.status_code == 200
    assert response


# def test_get_txs_latest_block() -> None:
#     url = settings.SERVER_HOST + "tx/block"
#
#     response = requests.get(url)
#     assert response.status_code == 200


def test_get_txs_by_height(prep_fixtures, client: TestClient):
    r = client.get(f"{settings.ICON_REST_API_PREFIX}/blocks/")
    response = r.json()
    latest_height = response[0]["number"]
    latest_hash = response[0]["hash"]

    r = client.get(f"{settings.ICON_REST_API_PREFIX}/tx/block/{latest_height}")
    response = r.json()
    assert r.status_code == 200
    assert response[0]["block_hash"] == latest_hash


# def test_get_txs_by_height() -> None:
#     url = settings.SERVER_HOST + "tx/block/10000000"
#
#     response = requests.get(url)
#     assert response.status_code == 200
