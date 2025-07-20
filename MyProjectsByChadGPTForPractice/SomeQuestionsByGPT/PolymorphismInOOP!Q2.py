# SINCE THE CHADGPT IS NOT WORKING IM USING GEMINI FOR QUES FOR THIS TOPIC 
# THIS IS THE QUESTION 
# 1.Create a base class Document. It should have an __init__ method taking a title. Include a method display_content() that prints "Displaying generic document content."
# 2.Create two subclasses: TextDocument and ImageDocument, both inheriting from Document.
# 3.Override display_content() in TextDocument to print the title and some sample text content specific to a text document.
# 4.Override display_content() in ImageDocument to print the title and a message indicating it's displaying an image, perhaps referencing an image filename.
 
class Document:
    def __init__(self, title):
        self.title = title

    def display_content(self):
        print("Displaying generic document content.")

class TextDocument(Document):
    def __init__(self, title, text_file):
        super().__init__(title)
        self.text_file = text_file
    
    def display_content(self):
        print(f"Diplaying Text Document: {self.title} ")
        print(f"Content: \n{self.text_file}\n")

class ImageDocument(Document):
    def __init__(self, title, image_file):
        super().__init__(title)
        self.image_file = image_file

    def display_content(self):
        print(f"Displaying Image DOcument: {self.title}")
        print(f"Image File: {self.image_file} - a beautiful landscape.\n")




 
        
doc1 = TextDocument("My Meeting Notes", "Attendees: Alice, Bob, Charlie.\nDiscussion: Project status update.")
doc2 = ImageDocument("Vacation Picture", "beach_sunset.jpg")

documents = [doc1, doc2]

def render_documents(documents_list):
    for doc in documents_list:
        doc.display_content()

render_documents(documents)  