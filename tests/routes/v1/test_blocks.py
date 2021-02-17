from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_block_latest(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.API_ENDPOINT_PREFIX}/blocks/")
    response = r.json()
    assert r.status_code == 200
    assert response


def test_get_block_by_height(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.API_ENDPOINT_PREFIX}/blocks/")
    response = r.json()
    latest_height = response[0]["number"]
    latest_hash = response[0]["hash"]

    r = client.get(f"{settings.API_ENDPOINT_PREFIX}/blocks/height/{latest_height}")
    response = r.json()
    assert r.status_code == 200
    assert response["hash"] == latest_hash


def test_get_block_by_height_error(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.API_ENDPOINT_PREFIX}/blocks/height/1000000000000000")
    response = r.json()
    assert r.status_code == 404
    assert response == {"detail": "Block not found"}


def test_get_block_by_hash(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.API_ENDPOINT_PREFIX}/blocks/")
    response = r.json()
    latest_height = response[0]["number"]
    latest_hash = response[0]["hash"]

    r = client.get(
        f"{settings.API_ENDPOINT_PREFIX}/blocks/hash/{latest_hash}"
    )
    response = r.json()
    assert r.status_code == 200
    assert response["number"] == latest_height


def test_get_block_by_hash_error(prep_fixtures, client: TestClient) -> None:
    r = client.get(
        f"{settings.API_ENDPOINT_PREFIX}/blocks/hash/1111111111111111111111fbcc7d17f5983570e8ddff6aff594d4dd44059"
    )
    response = r.json()
    assert r.status_code == 404
    assert response == {"detail": "Block not found"}
