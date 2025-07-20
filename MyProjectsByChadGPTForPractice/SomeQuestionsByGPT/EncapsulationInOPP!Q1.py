# MAKING CLASS STUDENT 
# MAKING ENCAPSULATION IN FUNCTION NAME AND MARKS 
# PRIVATE ATTRIBUTES :- __name and __marks 

class Student:
    def __init__(self, name, marks):
        self.__name = name 
        self.__marks = marks 

    def set_details(self, new_name, new_marks):
        self.__name = new_name
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid Marks Entered!")

    def get_detail(self):
        print(f"Name: {self.__name} \nMarks: {self.__marks}")
        

stu1 = Student("Mayuresh", 18)
stu1.get_detail()
stu1.set_details("Manya", 102)
stu1.get_detail()