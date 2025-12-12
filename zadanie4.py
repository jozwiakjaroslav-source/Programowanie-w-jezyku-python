
"""Utwórz funkcję, która otrzyma w parametrze listę 10 liczb (rekomendowane wykorzystanie funkcji range),
 a następnie wyświetli jedynie parzyste elementy."""


def wyswietl_parzyste(lista_liczb):
    print("Elementy parzyste z listy:")
    for liczba in lista_liczb:
        if liczba % 2 == 0:
            print(liczba)

lista_liczb = list(range(1, 21))
wyswietl_parzyste(lista_liczb)

