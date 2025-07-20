# Write a class Train which has methods to book a ticket, get status(no. of seats)
# and get a fare information of train running under Indian Railways

from random import randint

class Train:
    def __init__(self, trainNO):
        self.trainNO = trainNO
    def book(self, fro, to):
        print(f"Ticket is boooked in train no: {self.trainNO} from {fro} to {to}")
    def getStatus(self):
        print(f"Train no: {self.trainNO} is running on time")
    def getFare(self, fro, to):
        print(f"Fair of train ticket of train no: {self.trainNO} from {fro} to {to} is {randint(500, 5000)}")
        

t = Train(5313414)
t.book("Neral", "Kalyan")
t.getStatus()
t.getFare("Neral", "Kalyan")