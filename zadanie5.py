
"""Utwórz funkcję, która otrzyma w parametrze listę 10 liczb (rekomendowane wykorzystanie funkcji range),
 a następnie wyświetli co drugi element."""

def wyswietl_co_drugi(lista):
    print("Wyświetlanie co drugiego elementu listy:")
    co_drugi = lista[::2]
    print(co_drugi)

lista_10_liczb = list(range(1, 11))
print(f"Oryginalna lista: {lista_10_liczb}")
wyswietl_co_drugi(lista_10_liczb)