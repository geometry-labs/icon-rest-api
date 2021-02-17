from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_events_by_tx(prep_fixtures, client: TestClient):
    r = client.get(f"{settings.ICON_REST_API_PREFIX}/events/block")
    response = r.json()
    latest_hash = response[0]["transaction_hash"]


    r = client.get(
        f"{settings.ICON_REST_API_PREFIX}/events/tx/{latest_hash}"
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


def test_get_events_latest_block(prep_fixtures, client: TestClient):
    r = client.get(f"{settings.ICON_REST_API_PREFIX}/events/block")
    response = r.json()
    assert r.status_code == 200
    assert response


# def test_get_events_latest_block() -> None:
#     url = settings.SERVER_HOST + "events/block"
#
#     response = requests.get(url)
#     assert response.status_code == 200


def test_get_events_by_height(prep_fixtures, client: TestClient):
    r = client.get(f"{settings.ICON_REST_API_PREFIX}/blocks/")
    response = r.json()
    latest_height = response[0]["number"]
    latest_hash = response[0]["hash"]

    r = client.get(f"{settings.ICON_REST_API_PREFIX}/events/block/{latest_height}")
    response = r.json()
    assert r.status_code == 200
    assert response[0]["block_hash"] == latest_hash


# def test_get_events_by_height() -> None:
#     url = settings.SERVER_HOST + "tx/block/10000000"
#
#     response = requests.get(url)
#     assert response.status_code == 200
