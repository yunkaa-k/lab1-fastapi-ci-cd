from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_all_starts_empty():
    response = client.get("/api/items")
    assert response.status_code == 200
    assert response.json() == []


def test_create_item_returns_json_and_location():
    response = client.post(
        "/api/items", json={"name": "Notebook", "description": "For university"}
    )
    assert response.status_code == 201
    assert response.headers["content-type"].startswith("application/json")
    assert response.headers["location"] == "/api/items/1"
    assert response.json() == {
        "id": 1,
        "name": "Notebook",
        "description": "For university",
    }


def test_get_one_item():
    client.post("/api/items", json={"name": "Notebook"})
    response = client.get("/api/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Notebook"


def test_update_item():
    client.post("/api/items", json={"name": "Old"})
    response = client.put("/api/items/1", json={"name": "Updated"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated"


def test_delete_item():
    client.post("/api/items", json={"name": "Delete me"})
    response = client.delete("/api/items/1")
    assert response.status_code == 204
    assert response.content == b""
    assert client.get("/api/items/1").status_code == 404


def test_missing_item_returns_404():
    assert client.get("/api/items/777").status_code == 404
    assert client.put("/api/items/777", json={"name": "None"}).status_code == 404
    assert client.delete("/api/items/777").status_code == 404


def test_invalid_item_returns_422():
    response = client.post("/api/items", json={"name": ""})
    assert response.status_code == 422


def test_openapi_and_swagger_available():
    openapi = client.get("/openapi.json")
    assert openapi.status_code == 200
    assert "/api/items" in openapi.json()["paths"]
    assert client.get("/docs").status_code == 200
