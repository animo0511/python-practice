# Write a class 'Complex' to represent complex numbers, along the overload operators '+' and 'a' which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.i = i
        self.r = r

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)
    
    def __str__(self):
        if self.i >= 0:
            return (f"{self.r} + {self.i}i")
        else:
            return (f"{self.r} - {-self.i}i")
    
c1 = Complex(5, 9)
c2 = Complex(4, 6)
print(c1 + c2)
print(c1*c2)