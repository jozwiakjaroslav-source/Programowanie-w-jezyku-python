# Zadanie 3
def czy_parzysta(liczba: int) -> bool:
    return liczba % 2 == 0
liczba_do_sprawdzenia = 24
jest_parzysta = czy_parzysta(liczba_do_sprawdzenia)

print("\n--- Zadanie 3 ---")
if jest_parzysta:
    print(f"Liczba {liczba_do_sprawdzenia} jest parzysta")
else:
    print(f"Liczba {liczba_do_sprawdzenia} jest nieparzysta")
