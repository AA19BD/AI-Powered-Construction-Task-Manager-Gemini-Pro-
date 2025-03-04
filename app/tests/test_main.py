from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_project():
    response = client.post("/projects/", json={"project_name": "Bridge", "location": "NY"})
    assert response.status_code == 200
    assert response.json()["project_name"] == "Bridge"


def test_get_project_not_found():
    response = client.get("/projects/999")
    assert response.status_code == 404
