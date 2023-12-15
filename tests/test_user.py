from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_create_user():
    user_data = {"id": 2, "username": "newuser", "email": "newuser@example.com"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json()["username"] == "newuser"