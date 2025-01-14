class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Biblioteka w {self.city}, {self.street}, {self.zip_code}, "
                f"otwarta: {self.open_hours}, telefon: {self.phone}")


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
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
        return (f"Pracownik: {self.first_name} {self.last_name}, "
                f"zatrudniony: {self.hire_date}, "
                f"data urodzenia: {self.birth_date}, "
                f"adres: {self.city}, {self.street}, {self.zip_code}, "
                f"telefon: {self.phone}")


class Student:
    def __init__(self, first_name, last_name, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Student: {self.first_name} {self.last_name}, "
                f"adres: {self.city}, {self.street}, {self.zip_code}, "
                f"telefon: {self.phone}")


class Book:
    def __init__(
            self,
            library,
            publication_date,
            author_name,
            author_surname,
            number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Książka: {self.author_name} {self.author_surname}, "
            f"opublikowana: {self.publication_date}, "
            f"ilość stron: {self.number_of_pages}, "
            f"w bibliotece: [{self.library}]")


class Order:
    def __init__(self, employee, student, books: list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n  ".join(str(book) for book in self.books)
        return (f"Zamówione przez {self.employee}, "
                f"dla {self.student}, "
                f"w dniu {self.order_date}:\n  {books_str}")


biblioteka1 = Library(
    "Ruda Śląska", "Górnośląska", "41-717", "10:00-17:00", "536754887"
)
biblioteka2 = Library(
    "Katowice",
    "Sądowa",
    "40-153",
    "8:00-20:00",
    "526472858")

ksiazka1 = Book(biblioteka1, "12.04.2024", "Andrzej", "Kowalski", 135)
ksiazka2 = Book(biblioteka2, "13.05.1999", "Hans Christian", "Andersen", 200)
ksiazka3 = Book(biblioteka1, "12.12.2005", "Joanna", "Majewska", 196)
ksiazka4 = Book(biblioteka1, "31.08.2013", "Witold", "Kos", 43)
ksiazka5 = Book(biblioteka2, "01.01.1920", "Bolesław", "Prus", 800)

pracownik1 = Employee(
    "Krzysztof",
    "Niewiadomy",
    "12.06.2023",
    "08.12.2000",
    "Ruda Śląska",
    "Drozdów",
    "41-717",
    "746374829",
)
pracownik2 = Employee(
    "Kasia",
    "Kos",
    "04.05.2024",
    "04.09.1974",
    "Katowice",
    "Miejska",
    "40-234",
    "837566377",
)
pracownik3 = Employee(
    "Ola",
    "Bać",
    "18.02.2020",
    "21.08.1996",
    "Bytom",
    "Radoszowska",
    "40-237",
    "524374858",
)

student1 = Student(
    "Anna",
    "Nowak",
    "Ruda Śląska",
    "Drozdów",
    "41-717",
    "123456789")
student2 = Student(
    "Paweł",
    "Kowalski",
    "Katowice",
    "Sądowa",
    "40-153",
    "987654321")
student3 = Student("Ewa", "Maj", "Bytom", "Radoszowska", "40-237", "567890123")

zamowienie1 = Order(pracownik1, student1, [ksiazka1, ksiazka3], "23.07.2024")
zamowienie2 = Order(pracownik3, student2, [ksiazka2, ksiazka5], "12.12.2024")

print(zamowienie1)
print(zamowienie2)
