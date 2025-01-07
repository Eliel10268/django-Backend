import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_get_products():
    client = APIClient()
    response = client.get("/api/products/")
    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.django_db
def test_create_product():
    client = APIClient()
    new_product = {
        "name": "Test Product",
        "description": "A test product",
        "price": 10.99,
        "stock": 50
    }
    response = client.post("/api/products/", new_product, format="json")
    assert response.status_code == 201
    assert response.data["name"] == "Test Product"
