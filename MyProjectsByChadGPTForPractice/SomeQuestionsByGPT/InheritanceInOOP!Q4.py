# CREATING CLASS SMARTPHONE
# MAKING SUBCLASS NAMED AS IPHONE 

class Smartphone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def details(self):
        print(f"Smartphone: {self.brand}, Price: {self.price}")

class iPhone(Smartphone):
    def __init__(self, brand, price, model):
        super().__init__(brand, price)
        self.model = model

    def details(self):
        print(f"Smartphone: {self.brand} {self.model}, Price: {self.price}")

phone1 = Smartphone("Samsung", 50000)
phone2 = iPhone("iPhone", 70000, "13 Pro")

phone1.details()
phone2.details()