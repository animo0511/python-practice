# SINCE THE CHADGPT IS NOT WORKING IM USING GEMINI FOR QUES FOR THIS TOPIC 
# THIS IS THE QUESTION 
# 1.Create a base class Employee. This class should have an __init__ method that takes name and employee_id. It should also have a method calculate_salary() that prints a generic message like "Calculating generic employee salary."
# 2.Create two subclasses: FullTimeEmployee and Contractor, both inheriting from Employee.
# 3.Override the calculate_salary() method in FullTimeEmployee to calculate salary based on a monthly_salary attribute (e.g., self.monthly_salary).
# 4.Override the calculate_salary() method in Contractor to calculate salary based on an hourly_rate and hours_worked attributes (e.g., self.hourly_rate * self.hours_worked)
# 5.Create instances of both FullTimeEmployee and Contractor with appropriate data.
# 6.Store these employee objects in a single list.
# 7.Iterate through the list and call calculate_salary() for each employee, observing the polymorphic behavior.


class Employee:
    def __init__(self, name, employee_id):
        self.name = name 
        self.employee_id = employee_id

    def calculate_salary(self):
        print("Calculating generic employee salary,")

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary ):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        print(f"Full-time employee {self.name}'s salary: ${self.monthly_salary}")

class Contractor(Employee):
    def __init__(self, name, employee_id, hourly_rate, hourly_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hourly_worked = hourly_worked

    def calculate_salary(self):
        print(f"Contractor {self.name}'s salary: ${self.hourly_rate*self.hourly_worked}")
    

employee1 = FullTimeEmployee("John Doe", 405, 5000)
employee2 = Contractor("Jane Smith", 512, 400, 4)

employees = [employee1, employee2]

def calculate_salary(employees_list):
    for employee in employees_list:
        employee.calculate_salary()

calculate_salary(employees)

