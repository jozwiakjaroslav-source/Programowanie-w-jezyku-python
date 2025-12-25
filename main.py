from magazine.Product import Product
from magazine.Order import Order

if __name__ == "__main__":
    p1 = Product("Laptop", 3500.0)
    p2 = Product("Myszka", 120.50)
    p3 = Product("Monitor", 899.99)

    zamowienie = Order("Jarosław", [p1, p2, p3])

    print(p1)
    print("-" * 30)
    print(zamowienie)
