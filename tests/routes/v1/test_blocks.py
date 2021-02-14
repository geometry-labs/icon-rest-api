from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_block_latest(prep_blocks, client: TestClient) -> None:
    r = client.get(f"{settings.ICON_REST_API_ENDPOINT_PREFIX}/blocks/")
    response = r.json()
    assert r.status_code == 200
    assert response


def test_get_block_by_height(prep_blocks, client: TestClient) -> None:
    r = client.get(f"{settings.ICON_REST_API_ENDPOINT_PREFIX}/blocks/height/10000000")
    response = r.json()
    assert r.status_code == 200
    assert (
        response["hash"]
        == "d3ca23378c6bdef5e17eb9dfb4fbcc7d17f5983570e8ddff6aff594d4dd44059"
    )


def test_get_block_by_height_error(prep_blocks, client: TestClient) -> None:
    r = client.get(
        f"{settings.ICON_REST_API_ENDPOINT_PREFIX}/blocks/height/1000000000000000"
    )
    response = r.json()
    assert r.status_code == 404
    assert response == {"detail": "Block not found"}


def test_get_block_by_hash(prep_blocks, client: TestClient) -> None:
    r = client.get(
        f"{settings.ICON_REST_API_ENDPOINT_PREFIX}/blocks/hash/d3ca23378c6bdef5e17eb9dfb4fbcc7d17f5983570e8ddff6aff594d4dd44059"
    )
    response = r.json()
    assert r.status_code == 200
    assert response["number"] == 10000000


def test_get_block_by_hash_error(prep_blocks, client: TestClient) -> None:
    r = client.get(
        f"{settings.ICON_REST_API_ENDPOINT_PREFIX}/blocks/hash/1111111111111111111111fbcc7d17f5983570e8ddff6aff594d4dd44059"
    )
    response = r.json()
    assert r.status_code == 404
    assert response == {"detail": "Block not found"}
