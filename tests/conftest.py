import os
from typing import Generator

import pytest
from fastapi.testclient import TestClient

os.environ["ENV_FILE"] = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    ".env.test",
)

from main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
