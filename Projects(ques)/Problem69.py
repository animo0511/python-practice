# create a class(2-D Vector) and use it to create another class representing a 3-D Vector

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector equation is {self.i}i + {self.j}j")
        
class ThreeDVector(TwoDVector):
        def __init__(self, i, j, k):
            super().__init__(i, j)
            self.k = k
   
        def show(self):
            print(f"The vector equation is {self.i}i + {self.j}j + {self.k}k")
        

vec1 = TwoDVector(2, 4)
vec1.show()
vec2 = ThreeDVector(5, 9, 7)
vec2.show()