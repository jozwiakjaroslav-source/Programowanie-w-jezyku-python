class Student:

    def __init__(self, name: str, marks: list):

        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:

        if not self.marks:

            return False

        average_marks = sum(self.marks) / len(self.marks)

        return average_marks > 50


student1 = Student(name="Zuzia Wesoła", marks=[95, 75, 75, 75])

print(f"Student: {student1.name}")
print(f"Oceny: {student1.marks}")
print(f"Czy zaliczył (ma być True): {student1.is_passed()}")
print("-" * 20)

student2 = Student(name="Ignacy Ignatowicz", marks=[50, 40, 30, 40])

print(f"Student: {student2.name}")
print(f"Oceny: {student2.marks}")
print(f"Czy zaliczył (ma być False): {student2.is_passed()}")