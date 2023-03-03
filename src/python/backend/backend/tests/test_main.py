from backend.main import app
from fastapi.testclient import TestClient


def test_home():
    client = TestClient(app)
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"Hello": "World"}
