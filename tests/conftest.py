import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def api_client():
    from sunshine.app import app

    return TestClient(app)
