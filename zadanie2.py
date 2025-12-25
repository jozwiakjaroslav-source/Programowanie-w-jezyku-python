"""
Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych liczb,
 każdy jej element pomnoży przez 2, a na końcu ją zwróci
"""

#weraja pierwsza tj z uzyciem petli for

def mnozymy_przez_dwa(lista_startowa):
    lista_z_wynikami = []
    for liczba in lista_startowa:
        lista_z_wynikami.append(liczba * 2)
    return lista_z_wynikami

# --- Przykład użycia (Poprawiony) ---
liczby = [1, 2, 3, 4, 5]
wynik = mnozymy_przez_dwa(liczby)




print(wynik)
