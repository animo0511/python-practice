# Program to calculate the grade of a student from his marks from the following scheme
'''90-100=>Ex
   80-90=>A
   70-80=>B
   60-70=>C
   50-60=>D
   <50=>F'''

marks = int(input("Enter your marks:"))

if 100>marks>90:
    print("You got \"Ex\" grade")
elif 90>marks>80:
    print("You got \"A\" grade")
elif 80>marks>70:
    print("Your got \"B\" grade")
elif 70>marks>60:
    print("You got \"C\" grades")
elif 60>marks>50:
    print("You got \"D\" grades")
else:
    print("Your got \"F\" grades")                    