# Zadanie 4
"""Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi
czy suma dwóch pierwszych liczb jest większa lub równa trzeciej,
 a następnie zwróci tę informację jako typ logiczny bool"""


def porownaj_sume(a: int, b: int, c: int) -> bool:
    return (a + b) >= c


wynik_porownania = porownaj_sume(10, 5, 12)

print("\n--- Zadanie 4 ---")
print(f"Czy suma (10 + 5) jest >= 12? {wynik_porownania}")
