import pytest
from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_get_products(client):
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.get_json()) == 3


def test_get_single_product(client):
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.get_json()["name"] == "Laptop"


def test_get_product_not_found(client):
    response = client.get("/products/999")
    assert response.status_code == 404


def test_add_to_cart(client):
    response = client.post("/cart/add", json={"product_id": 2})
    assert response.status_code == 201


def test_add_to_cart_missing_id(client):
    response = client.post("/cart/add", json={})
    assert response.status_code == 400


def test_add_to_cart_invalid_product(client):
    response = client.post("/cart/add", json={"product_id": 999})
    assert response.status_code == 404
