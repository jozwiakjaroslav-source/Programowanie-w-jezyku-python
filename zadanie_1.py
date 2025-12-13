class Student:
    """
    Klasa reprezentująca studenta z imieniem i listą ocen.
    """
    def __init__(self, name: str, marks: list[int]):
        """
        Konstruktor klasy Student. Inicjalizuje imię i listę ocen.

        :param name: Imię studenta (string).
        :param marks: Lista ocen studenta (lista liczb całkowitych).
        """
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        """
        Metoda sprawdzająca, czy student zdał.
        Student zdaje, jeśli średnia jego ocen jest większa niż 50.

        :return: True, jeśli średnia ocen > 50; False w przeciwnym razie.
        """
        if not self.marks:
            # Zabezpieczenie przed dzieleniem przez zero, jeśli lista ocen jest pusta
            return False

        # 1. Obliczenie sumy ocen
        total_marks = sum(self.marks)

        # 2. Obliczenie średniej
        average_mark = total_marks / len(self.marks)

        print(f"Średnia ocen dla {self.name}: {average_mark:.2f}")

        # 3. Sprawdzenie warunku zdania (> 50)
        return average_mark > 50

# --- Przykładowe Obiekty Klasy ---

### Obiekt 1: Wynikający True (Student, który zdał)
# Średnia: (70 + 85 + 60 + 90) / 4 = 305 / 4 = 76.25 ( > 50)
student_passed = Student("Anna Kowalska", [70, 85, 60, 90])
print(f"\nCzy {student_passed.name} zdał(a)? {student_passed.is_passed()}")

print("-" * 40)

### Obiekt 2: Wynikający False (Student, który nie zdał)
# Średnia: (40 + 50 + 35 + 55) / 4 = 180 / 4 = 45.00 ( <= 50)
student_failed = Student("Piotr Nowak", [40, 50, 35, 55])
print(f"\nCzy {student_failed.name} zdał(a)? {student_failed.is_passed()}")