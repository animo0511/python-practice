# CREATING CLASS NAMED AS Shape 
# IT HAS A METHOD area()
# THERE ARE TWO SUBCLASSES AS Circle AND Square

class Shape:
    def __init__(self):
        pass

    def area(self):
        print("Area: ")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius 
    
    def area(self):
        print(f"Circle Area: {3.14 * self.radius * self.radius}")

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side 

    def area(self):
        print(f"Square Area: {self.side * self.side}")

area1 = Circle(5)
area2 = Square(4)

for areas in [area1, area2]:
    areas.area()
    
