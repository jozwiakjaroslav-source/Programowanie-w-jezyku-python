# Zadanie 1
"""Stworzyć funkcję, która przyjmuje 2 argumenty (typu string) name i surname,
a następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}!
 Należy uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie go wyświetlić (print)
"""


def stworz_powitanie(name: str, surname: str) -> str:
    return f"Cześć {name} {surname}!"


wynik_powitania = stworz_powitanie("Tomek", "Tomkowski")

print("--- Zadanie 1 ---")
print(wynik_powitania)
