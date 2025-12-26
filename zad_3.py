# Zadanie 3
"""Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba
w parametrze jest parzysta i zwróci tą informację jako typ logiczny bool (True/False).
Należy uruchomić funkcję, wynik wykonania zapisać do zmiennej,
 a następnie wykorzystując warunek logiczny wyświetlić prawidłowy tekst
  "Liczba parzysta" / "Liczba nieparzysta"""


def czy_parzysta(liczba: int) -> bool:
    return liczba % 2 == 0


liczba_do_sprawdzenia = 24
jest_parzysta = czy_parzysta(liczba_do_sprawdzenia)

print("\n--- Zadanie 3 ---")
if jest_parzysta:
    print(f"Liczba {liczba_do_sprawdzenia} jest parzysta")
else:
    print(f"Liczba {liczba_do_sprawdzenia} jest nieparzysta")
