import pytest


def test_get_existing_user(client):
    response = client.get("/users/1")

    assert response.status_code == 200
    assert response.get_json()["name"] == "Farida"


def test_get_missing_user_returns_404(client):
    response = client.get("/users/999")

    assert response.status_code == 404
    assert response.get_json() == {"error": "User not found"}


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"role": "qa"},
        {"name": ""},
    ],
)
def test_create_user_without_name_returns_400(client, payload):
    response = client.post("/users", json=payload)

    assert response.status_code == 400
    assert response.get_json() == {"error": "Name is required"}


def test_create_user_returns_201(client):
    response = client.post(
        "/users",
        json={"name": "Test User", "role": "qa"},
    )

    assert response.status_code == 201
    body = response.get_json()

    assert body["name"] == "Test User"
    assert body["role"] == "qa"
    assert isinstance(body["id"], int)
