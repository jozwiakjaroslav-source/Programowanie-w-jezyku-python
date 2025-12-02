def wyswietl_liczby_parzyste(lista_liczb):
    for i in range (len(lista_liczb)):
        x = lista_liczb[i]
        if x % 2 == 0:
            print(x)


moja_lista = [10, 15, 22, 33, 40, 55, 60]
print("Parzyste elementy to:")
wyswietl_liczby_parzyste(moja_lista)