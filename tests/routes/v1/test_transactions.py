import requests
from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_tx_by_hash(prep_transactions, client: TestClient):
    # TODO: Fix me -> from conftest OverflowError: MongoDB can only handle up to 8-byte ints
    r = client.get(
        f"{settings.ICON_REST_API_ENDPOINT_PREFIX}/tx/hash/0xc065e6070af781b64bda7dac6d323779486a81e9409bc49514059125ea6e750c"
    )
    response = r.json()
    assert r.status_code == 200
    assert response


# def test_get_tx_by_hash() -> None:
#     url = (
#         settings.SERVER_HOST
#         + "tx/hash/0xd007cf25e28a98066f27a6ea113e41c34a3deaf91a1e17456949714997f9e642"
#     )
#
#     response = requests.get(url)
#     assert response.status_code == 200


def test_get_txs_latest_block(prep_transactions, client: TestClient):
    r = client.get(f"{settings.ICON_REST_API_ENDPOINT_PREFIX}/tx/block")
    response = r.json()
    assert r.status_code == 200
    assert response


# def test_get_txs_latest_block() -> None:
#     url = settings.SERVER_HOST + "tx/block"
#
#     response = requests.get(url)
#     assert response.status_code == 200


def test_get_txs_by_height(prep_transactions, client: TestClient):
    r = client.get(f"{settings.ICON_REST_API_ENDPOINT_PREFIX}/tx/block/10000000")
    response = r.json()
    assert r.status_code == 200
    assert response


# def test_get_txs_by_height() -> None:
#     url = settings.SERVER_HOST + "tx/block/10000000"
#
#     response = requests.get(url)
#     assert response.status_code == 200
