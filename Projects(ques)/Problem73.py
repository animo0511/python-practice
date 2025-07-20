# Write a class 'Vector' representing a vector of n dimentions. Overloadthe '+' and '*' operator which calculates the sum and the dot(.) product of them

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k 

    def __add__(self, other):
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)
    
    def __mul__(self, other):
        return (self.i*other.i + self.j*other.j + self.k*other.k)

    def __str__(self):
        return (f"Vector {self.i}i + {self.j}j + {self.k}k")

vec1 = Vector(2, 6, 8)
vec2 = Vector(6, 3, 8)

print(vec1 + vec2)
print(vec1*vec2)
    

        