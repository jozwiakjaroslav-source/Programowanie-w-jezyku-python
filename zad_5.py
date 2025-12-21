# Zadanie 5
def czy_lista_zawiera(lista_elementow: list, szukana_wartosc: int) -> bool:
    return szukana_wartosc in lista_elementow

lista_ocen = [10, 20, 35, 40, 50]
szukana_liczba = 35
wynik_zawierania = czy_lista_zawiera(lista_ocen, szukana_liczba)

print("\n--- Zadanie 5 ---")
print(f"Lista: {lista_ocen}")
print(f"Czy lista zawiera liczbę {szukana_liczba}? {wynik_zawierania}")