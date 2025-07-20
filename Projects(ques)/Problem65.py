# Write a "calculator" capable of finding square, cube and sqaure root of a number

class Calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The square is:{self.n*self.n}")
    def cube(self):
        print(f"Cube is: {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"Cube root is: {self.n**1/2}")

num = Calculator(4)
num.square()
num.cube()
num.squareroot()