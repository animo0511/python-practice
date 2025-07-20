# TO FIX THE FOLLOWING CODE 
'''class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

emp = Employee("Mayuresh", 30000)
emp.__salary = 20000  # This should NOT be allowed directly
print(emp.__salary)   # This should NOT work'''

class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.__salary = salary
    
    def set_new_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print(f"Your salary is updated to {new_salary}rs. from {self.__salary}")
        else:
            print("New salary cant be less than current salary.")

    def get_salary(self):
        print(f"Mr. {self.name}'s salary is {self.__salary}rs.")

emp = Employee("Mayuresh", 30000)
emp.set_new_salary(100000)
emp.get_salary()