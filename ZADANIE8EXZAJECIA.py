import requests
import argparse

class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str, city: str, state: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.state = state

    def __str__(self) -> str:
        return f"Browar: {self.name} | Typ: {self.brewery_type} | Miasto: {self.city}, {self.state}"

parser = argparse.ArgumentParser(description="Pobiera listę browarów z API.")
parser.add_argument('--city', type=str, help='Nazwa miasta, z którego chcesz pobrać browary')
args = parser.parse_args()

base_url = "https://api.openbrewerydb.org/v1/breweries"
params = {"per_page": 20}

if args.city:
    params["by_city"] = args.city


odpowiedz = requests.get(base_url, params=params)
dane_surowe = odpowiedz.json()

lista_obiektow_browarow = []

for element in dane_surowe:
    nowy_browar = Brewery(
        id=element.get('id'),
        name=element.get('name'),
        brewery_type=element.get('brewery_type'),
        city=element.get('city'),
        state=element.get('state')
    )
    lista_obiektow_browarow.append(nowy_browar)

print(f"--- WYNIK ZADANIA: LISTA BROWARÓW (Filtr: {args.city if args.city else 'Wszystkie'}) ---\n")
for browar in lista_obiektow_browarow:
    print(browar)