# MAKING CLASS OF EMPLOYEE
# AND SUBCLASSSE NAMED AS MANAGER
# We will override the function named as show_details()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show_details(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_details(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")
        print(f"Manager of {self.department}")

person = Manager("Mayuresh", 3000000, "IT department")
person.show_details()