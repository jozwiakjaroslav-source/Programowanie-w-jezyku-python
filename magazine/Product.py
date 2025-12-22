from magazine.utils import format_price

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Produkt: {self.name} | Cena: {format_price(self.price)}"