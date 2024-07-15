from datetime import datetime
from .models import Product
from .exceptions import InsertError, NotFoundError

class ProductController:
    def __init__(self):
        self.products = {}
        self.next_id = 1

    def create_product(self, name, price):
        try:
            if not name or not price:
                raise ValueError("Nome e preço são obrigatórios")
            product = Product(name, price)
            product.id = self.next_id
            self.products[self.next_id] = product
            self.next_id += 1
            return product
        except Exception as e:
            raise InsertError(f"Erro ao inserir o produto: {e}")

    def update_product(self, product_id, name=None, price=None):
        if product_id not in self.products:
            raise NotFoundError("Produto não encontrado")

        product = self.products[product_id]
        if name:
            product.name = name
        if price:
            product.price = price
        product.updated_at = datetime.utcnow()
        return product

    def filter_products_by_price(self, min_price, max_price):
        return [p for p in self.products.values() if min_price < p.price < max_price]
