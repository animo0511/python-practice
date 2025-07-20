# create a class "Prgrammmer" for storing information of few programmers workin at Microsoft

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Mayuresh", 170000, 421306)

print(p.name, p.salary, p.pin, p.company)
