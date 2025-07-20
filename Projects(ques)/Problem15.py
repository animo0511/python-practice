# Program to acccept marks of 6 students and displays them in a sorted manner
 
marks = [] 

student1 = int(input("Enter your mark:"))
marks.append(student1)
student2 = int(input("Enter your mark:"))
marks.append(student2)
student3 = int(input("Enter your mark:"))
marks.append(student3)
student4 = int(input("Enter your mark:"))
marks.append(student4)
student5 = int(input("Enter your mark:"))
marks.append(student5)
student6 = int(input("Enter your mark:"))
marks.append(student6)

marks.sort()
marks.reverse()
print(marks)
