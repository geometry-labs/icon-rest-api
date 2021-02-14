import json
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

from app.db.session import MongoClient
from app.main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


def insert_fixture(fixture):
    client = MongoClient
    with open(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "fixtures", fixture + ".json"
        )
    ) as f:
        fixture_json = json.load(f)
    db = client["icon"]
    db.blocks.insert_many(fixture_json)


@pytest.fixture()
def prep_blocks():
    insert_fixture("blocks")
    yield
    client = MongoClient
    db = client["icon"]
    db.blocks.remove({})


@pytest.fixture()
def prep_transactions():
    insert_fixture("transactions")
    yield
    client = MongoClient
    db = client["icon"]
    db.blocks.remove({})


@pytest.fixture()
def prep_logs():
    insert_fixture("logs")
    yield
    client = MongoClient
    db = client["icon"]
    db.blocks.remove({})
