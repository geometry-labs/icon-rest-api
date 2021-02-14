from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_events_by_tx(prep_logs, client: TestClient):
    r = client.get(
        f"{settings.API_ENDPOINT_PREFIX}/events/tx/0xfd418771ac80e983c3c8edcde41c9fbfa40493b9c5c92dde7c155e5925418ce6"
    )
    response = r.json()
    assert r.status_code == 200
    assert response


# def test_get_events_by_tx() -> None:
#     url = (
#             settings.SERVER_HOST
#             + "events/tx_hash/0xd007cf25e28a98066f27a6ea113e41c34a3deaf91a1e17456949714997f9e642"
#     )
#
#     response = requests.get(url)
#     assert response.status_code == 200


def test_get_events_latest_block(prep_logs, client: TestClient):
    r = client.get(f"{settings.API_ENDPOINT_PREFIX}/events/block")
    response = r.json()
    assert r.status_code == 200
    assert response


# def test_get_events_latest_block() -> None:
#     url = settings.SERVER_HOST + "events/block"
#
#     response = requests.get(url)
#     assert response.status_code == 200


def test_get_events_by_height(prep_logs, client: TestClient):
    r = client.get(f"{settings.API_ENDPOINT_PREFIX}/tx/block/10000000")
    response = r.json()
    assert r.status_code == 200
    assert response


# def test_get_events_by_height() -> None:
#     url = settings.SERVER_HOST + "tx/block/10000000"
#
#     response = requests.get(url)
#     assert response.status_code == 200
