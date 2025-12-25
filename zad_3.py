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


house1 = House(
    area=145.0,
    rooms=6,
    price=590000.00,  # Obniżona cena
    address="ul. Jana Ostroroga 24, Poznań",
    plot=650
)

flat1 = Flat(
    area=48.5,
    rooms=2,
    price=315000.00,  # Okazyjna cena
    address="ul. Szamarzewskiego 12/4, Poznań",
    floor=2
)


flat2 = Flat(
    area=62.0,
    rooms=3,
    price=399000.00,
    address="ul. Wierzbięcice 38/10, Poznań",
    floor=1
)

print("=" * 40)
print("WYŚWIETLENIE NIERUCHOMOŚCI W POZNANIU:")
print("=" * 40)
print(house1)
print("\n" + "-" * 20)
print(flat1)
print("\n" + "-" * 20)
print(flat2)