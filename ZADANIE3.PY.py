class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"--- DOM ---\n"
                f"Adres: {self.address}\n"
                f"Powierzchnia domu: {self.area} m2\n"
                f"Działka: {self.plot} m2\n"
                f"Pokoje: {self.rooms}\n"
                f"Cena: {self.price:.2f} PLN")


class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"--- MIESZKANIE ---\n"
                f"Adres: {self.address}\n"
                f"Powierzchnia mieszkania: {self.area} m2\n"
                f"Piętro: {self.floor}\n"
                f"Pokoje: {self.rooms}\n"
                f"Cena: {self.price:.2f} PLN")

# ====================================================================
# TWORZENIE I WYŚWIETLENIE OBIEKTÓW
# ====================================================================

house1 = House(
    area=120.5,
    rooms=5,
    price=650000.00,
    address="ul. Słoneczna 15, Poznań",
    plot=800
)

flat1 = Flat(
    area=55.0,
    rooms=3,
    price=420000.00,
    address="al. Niepodległości 2/7, Kraków",
    floor=3
)

print("=" * 40)
print("WYŚWIETLENIE DOMU:")
print("=" * 40)
print(house1)

print("\n" + "=" * 40)
print("WYŚWIETLENIE MIESZKANIA:")
print("=" * 40)
print(flat1)