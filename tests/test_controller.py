import pytest
from controller import ProductController, InsertError, NotFoundError

def test_create_product():
    controller = ProductController()
    product = controller.create_product("Produto 1", 6000)
    assert product.name == "Produto 1"
    assert product.price == 6000

def test_create_product_error():
    controller = ProductController()
    with pytest.raises(InsertError):
        controller.create_product("", None)

def test_update_product_not_found():
    controller = ProductController()
    with pytest.raises(NotFoundError):
        controller.update_product(999, name="Produto Atualizado")

def test_filter_products_by_price():
    controller = ProductController()
    controller.create_product("Produto 1", 6000)
    controller.create_product("Produto 2", 9000)
    products = controller.filter_products_by_price(5000, 8000)
    assert len(products) == 1
    assert products[0].name == "Produto 1"
