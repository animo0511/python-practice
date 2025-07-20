# Add a static method in problem 2, to greet the user hello

class Calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The square is:{self.n*self.n}")
    def cube(self):
        print(f"Cube is: {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"Cube root is: {self.n**1/2}")
    @staticmethod
    def hello():
        print("Hello!")

num = Calculator(4)
num.square()
num.cube()
num.squareroot()
num.hello()