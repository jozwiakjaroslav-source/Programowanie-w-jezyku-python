# Zadanie 4
def porownaj_sume(a: int, b: int, c: int) -> bool:
    return (a + b) >= c

wynik_porownania = porownaj_sume(10, 5, 12)

print("\n--- Zadanie 4 ---")
print(f"Czy suma (10 + 5) jest >= 12? {wynik_porownania}")