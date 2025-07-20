# Program to find out wheather a student has passed or failed 
# It requires total of 40% at least 33% in each subject to pass
# Assume 3 subjects and take marks as an input from the user

# I'm letting the 3 subs are PCM

sub1 = int(input("Enter Your Maths Marks:"))
sub2 = int(input("Enter Your Physics Marks:"))
sub3 = int(input("Enter Your Chemistry Marks:"))

percentage = ((sub1+sub2+sub3)/300)*100

if sub1>33 and sub2>33 and sub3>33 and percentage>40:
    print("You Passed the Exam by", percentage, "% marks.")

else:
    print("You Failed the exam")