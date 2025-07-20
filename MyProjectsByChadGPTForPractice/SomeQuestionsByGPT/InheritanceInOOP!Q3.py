# MAKING CLASS OF ANIMAL 
# CREATING SUBCLASS NAMED AS DOG

class Animal:
    def __init__(self, name):
        self.name = name 
    
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        print(f"Bark! I am {self.name}")

animal1 = Animal("Dog")
animal2 = Dog("Rocky")

animal1.speak()
animal2.speak()