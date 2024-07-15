from datetime import datetime

class Product:
    def __init__(self, name, price):
        self.id = None  # O ID será atribuído pelo banco de dados
        self.name = name
        self.price = price
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
