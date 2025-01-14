class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        srednia = sum(self.marks) / len(self.marks)
        return srednia > 3


uczen1 = Student("Anna", [5, 4, 3, 6, 3, 5, 3, 6, 3, 5, 3])
uczen2 = Student("Karolina", [2, 4, 3, 6, 4, 3, 1, 1, 3, 2, 5, 2])

print(uczen1.name, ":", uczen1.is_passed())
print(uczen2.name, ":", uczen2.is_passed())
