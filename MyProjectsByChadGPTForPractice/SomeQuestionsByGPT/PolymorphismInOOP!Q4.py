# CREATING CLASS NAMED AS Device
# THIS CLASS HAVE use() METHOD 
# THERE ARE TWO SUBCLASSES NAMED AS Laptop AND Phone 

class Device:
    def __init__(self, work):
        self.work = work

    def use(self):
        print(f"Using device for {self.work}")

class Laptop(Device):
    def __init__(self, work):
        super().__init__(work)
    
    def use(self):
        print(f"Using the Laptop for {self.work}")

class Phone(Device):
    def __init__(self, work):
        super().__init__(work)
    
    def use(self):
        print(f"Using the Phone for {self.work}")

device1 = Laptop("coding")
device2 = Phone("calling")

for devices in [device1, device2]:
    devices.use()


        