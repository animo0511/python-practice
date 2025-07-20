# MAKING CLASS VEHICLE
# CREATING CHILD CLASS NAMED AS CAR
# ANOTHER CHILD CLASS NAMED AS BOAT 
# We will going to overrides the move() function everytime

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def move(self):
        print(f"The {self.brand} vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print(f"The {self.brand} car is driving on the road.")

class Boat(Vehicle):
    def move(self):
        print(f"The {self.brand} boat is sailing on the water.")

    
first = Vehicle("Lamborghini")
second = Car("Toyota")
third = Boat("Boston Whaler")

first.move()
second.move()
third.move()