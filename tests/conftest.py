import os
from typing import Generator

import pytest
from fastapi.testclient import TestClient

ENVIRONMENT = os.environ.get("ENVIRONMENT", "local")
if ENVIRONMENT == "local":
    # `.env.local` should be ignored in dockerignore so as to fail in container
    os.environ["ENV_FILE"] = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), ".env.local"
    )

from main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
