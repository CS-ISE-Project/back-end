from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "item1"

def test_create_item():
    item_data = {"id": 2, "name": "newitem", "description": "A new item"}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json()["name"] == "newitem"