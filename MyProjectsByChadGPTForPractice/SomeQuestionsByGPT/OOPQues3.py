# MAKING A PERSON CLASS 

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

person1 = Person("Mayuresh", 17)
person2 = Person("Prathamesh", 17)

person1.introduce()
print(person2.age)