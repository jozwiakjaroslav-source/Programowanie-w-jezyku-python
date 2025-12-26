# Zadanie 2


class Library:

    def __init__(
        self, city: str, street: str, zip_code: str, open_hours: str, phone: str
    ):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka w {self.city}, ul. {self.street} ({self.zip_code}). Godziny: {self.open_hours}"


class Employee:

    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: str,
        birth_date: str,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name} (Zatrudniony: {self.hire_date})"


class Student:
    """Klasa pomocnicza opisująca studenta/czytelnika, potrzebna w klasie Order."""

    def __init__(self, first_name: str, last_name: str, student_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name} (ID: {self.student_id})"


class Book:
    """Klasa opisująca książkę, która przechowuje obiekt Library."""

    def __init__(
        self,
        library: Library,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
        title: str,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
        self.title = title

    def __str__(self):
        # Użycie atrybutów z obiektu Library wewnątrz __str__ Book
        biblioteka_info = self.library.city
        return (
            f"Książka: '{self.title}' Autor: {self.author_surname} ({self.publication_date}, "
            f"{self.number_of_pages} str.). Pochodzi z biblioteki w: {biblioteka_info}"
        )


class Order:

    def __init__(
        self, employee: Employee, student: Student, books: list[Book], order_date: str
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        # Tworzenie czytelnej listy wypożyczonych książek
        ksiazki_str = "\n".join(
            [f"    - '{book.title}' ({book.author_surname})" for book in self.books]
        )

        return (
            f"--- ZAMÓWIENIE Z DNIA {self.order_date} ---\n"
            f"Pracownik obsługujący: {self.employee.first_name} {self.employee.last_name}\n"
            f"Odbiorca: {self.student.first_name} {self.student.last_name}\n"
            f"Wypożyczone książki ({len(self.books)}):\n{ksiazki_str}\n"
            f"------------------------------------"
        )


library1 = Library("Poznań", "Poznanska 10", "61-100", "8:00-18:00", "123-123-123")
library2 = Library("Poznań", "Wrocławska 20", "61-150", "9:00-17:00", "555-555-555")


employee1 = Employee(
    "Anna",
    "Kowalska",
    "2020-05-01",
    "1990-01-01",
    "Kraków",
    "Słoneczna 1",
    "30-100",
    "111-222-333",
)
employee2 = Employee(
    "Piotr",
    "Nowak",
    "2018-10-15",
    "1985-11-20",
    "Warszawa",
    "Mokra 2",
    "01-001",
    "444-555-666",
)
employee3 = Employee(
    "Ewa",
    "Lis",
    "2022-01-20",
    "1995-07-25",
    "Kraków",
    "Główna 3",
    "30-200",
    "777-888-999",
)


student1 = Student("Marek", "Zieliński", 1001)
student2 = Student("Iga", "Swiątek", 1002)
student3 = Student("Tomek", "Borowski", 1003)


book1 = Book(library1, "1905-01-01", "Henryk", "Sienkiewicz", 320, "Potop")
book2 = Book(library1, "1890-01-01", "Bolesław", "Prus", 700, "Lalka")
book3 = Book(library2, "2002-10-15", "Andrzej", "Sapkowski", 400, "Ostatnie życzenie")
book4 = Book(library2, "1961-12-01", "Stanisław", "Lem", 250, "Solaris")
book5 = Book(library1, "1937-10-01", "Witold", "Gombrowicz", 300, "Ferdydurke")


order1 = Order(
    employee=employee1,
    student=student1,
    books=[book1, book5, book2],
    order_date="2025-12-14",
)

order2 = Order(
    employee=employee2, student=student2, books=[book3, book4], order_date="2025-12-14"
)


print("\n" + "=" * 40)
print("WYŚWIETLENIE ZAMÓWIEŃ:")
print("=" * 40)

print(order1)

print("\n" + "#" * 40 + "\n")

print(order2)
print("\n" + "=" * 40)
