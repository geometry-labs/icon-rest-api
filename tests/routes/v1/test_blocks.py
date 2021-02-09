import requests

from app.core.config import settings


def test_get_block_latest() -> None:
    url = settings.SERVER_HOST + "blocks/"

    response = requests.get(url)
    assert response.status_code == 200


def test_get_block_by_height() -> None:
    url = settings.SERVER_HOST + "blocks/height/10000000"

    response = requests.get(url)
    assert response.status_code == 200


def test_get_block_by_hash() -> None:
    url = (
        settings.SERVER_HOST
        + "blocks/hash/ee0077a8bb433897ca7e00b52e0bdb461cf4c356ec817cd47a6570aa172b37dc"
    )

    response = requests.get(url)
    assert response.status_code == 200
