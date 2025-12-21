# Zadanie 6
def przetworz_listy(lista1: list, lista2: list) -> list:
    polaczona_lista = lista1 + lista2
    unikalne_elementy = list(set(polaczona_lista))


    przetworzona_lista = [element ** 3 for element in unikalne_elementy]

    return przetworzona_lista



lista_a = [1, 2, 3, 5]
lista_b = [3, 4, 5, 6, 6]
wynik_przetwarzania = przetworz_listy(lista_a, lista_b)

print("\n--- Zadanie 6 ---")
print(f"Lista 1: {lista_a}")
print(f"Lista 2: {lista_b}")
print(f"Wynik (unikalne, podniesione do potęgi 3): {wynik_przetwarzania}")
# Oczekiwane unikalne elementy: [1, 2, 3, 4, 5, 6]
# Oczekiwane potęgi (np. 5**3 = 125, 6**3 = 216)