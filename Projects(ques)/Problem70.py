# Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. Add method 'bark' to class 'Dog'

class Animals:
        pass

class Pets(Animals):
        pass

class Dog(Pets):
    def bark(self):
        print("Bow Bow !")

    """OR we can use
    @staticmethod
    def bark():
        print("Bow Bow !")"""

a = Dog()
a.bark()