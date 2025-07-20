class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def show(self):
        print(f"Name: {self.__name}, Grade: {self.__grade}")

s = Student("Maya", "A")
print(s.__name)
