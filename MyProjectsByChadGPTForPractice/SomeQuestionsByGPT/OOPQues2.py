# MAKING BIKE CLASS 

class Bike:
    def __init__(self, brand, engine_cc):
        self.brand = brand
        self.engine_cc = engine_cc
    
    def start(self):
        print(f"The {self.brand} bike with {self.engine_cc} cc engine has started.")

bike1 = Bike("Kawasaki Ninja ZX-10R", 998)
bike2 = Bike("Ducati Panigale V4", 1103)

bike1.start()
bike2.start()