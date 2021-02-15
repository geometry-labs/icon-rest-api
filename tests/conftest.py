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


def insert_fixture(fixture, collection_name=""):
    if collection_name == "":
        collection_name = fixture

    client = MongoClient

    # Read fixture
    with open(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "fixtures", fixture + ".json"
        )
    ) as f:
        fixture_json = json.load(f)

    # Populate collection
    db = client["icon"]
    db[collection_name].insert_many(fixture_json)


@pytest.fixture()
def prep_blocks():
    insert_fixture("blocks")
    yield

    # Clean up
    client = MongoClient
    db = client["icon"]
    db["blocks"].remove({})


@pytest.fixture()
def prep_transactions():
    insert_fixture("transactions")
    yield

    # Clean up
    client = MongoClient
    db = client["icon"]
    db["transactions"].remove({})


@pytest.fixture()
def prep_logs():
    insert_fixture("logs", "events")
    yield

    # Clean up
    client = MongoClient
    db = client["icon"]
    db["events"].remove({})
