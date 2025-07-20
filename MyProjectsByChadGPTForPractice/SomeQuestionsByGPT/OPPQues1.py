# MAKING A CLASS OF BOOK

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author  
    
    def display(self):
        print(f"Book: {self.title} by {self.author}")
    

book1 = Book("Clean Code: A Handbook of Agile Software Craftsmanship", "Robert C. Martin")
book2 = Book("The Pragmatic Programmer: From Journeyman to Master", "Andrew Hunt and David Thomas")

book1.display()
book2.display()