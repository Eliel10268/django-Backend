import pytest
from products.models import Product

@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        name="Test Product",
        description="Test Description",
        price=19.99,
        stock=100
    )
    assert product.name == "Test Product"
    assert product.stock == 100
