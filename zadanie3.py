"""Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych liczb,
 każdy jej element pomnoży przez 2, a na końcu ją zwróci."""

def pomnoz_przez_dwa_skladana(liczby_podstawowe):
    return [liczba * 2 for liczba in liczby_podstawowe]

liczby_podstawowe = [5, 10, 15, 20, 25]
wynik = pomnoz_przez_dwa_skladana(liczby_podstawowe)

print(f"Wynik po pomnożeniu przez 2: {wynik}")