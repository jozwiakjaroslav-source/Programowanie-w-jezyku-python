from magazine.utils import format_price
from magazine.Product import Product

class Order:
    def __init__(self, employee: str, products: list[Product]):
        self.employee = employee
        self.products = products

    def __str__(self):
        lista_p = "\n".join([f"- {p.name}" for p in self.products])
        return f"Zamówienie (Obsługa: {self.employee}):\n{lista_p}"
