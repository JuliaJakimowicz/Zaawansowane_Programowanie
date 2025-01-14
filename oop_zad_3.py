class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (f"Cena: {self.price}, ilosć pokoi: {self.rooms}, "
                f"metraż: {self.area}, adres: {self.address}")


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"{super().__str__()}, Rozmiar działki: {self.plot}"


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"{super().__str__()}, Piętro: {self.floor}"


mieszkanie = Flat("75 m2", 4, "33000 zł", "Drozdów", "4")
dom = House("120 m2", 7, "1000000 zł", "Sadowa", 200)

print(mieszkanie)
print(dom)
