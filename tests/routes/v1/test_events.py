import requests

from app.core.config import settings


def test_get_events_by_tx() -> None:
    url = (
        settings.SERVER_HOST
        + "events/tx_hash/0xd007cf25e28a98066f27a6ea113e41c34a3deaf91a1e17456949714997f9e642"
    )

    response = requests.get(url)
    assert response.status_code == 200


def test_get_events_latest_block() -> None:
    url = settings.SERVER_HOST + "events/block"

    response = requests.get(url)
    assert response.status_code == 200


def test_get_events_by_height() -> None:
    url = settings.SERVER_HOST + "tx/block/10000000"

    response = requests.get(url)
    assert response.status_code == 200
