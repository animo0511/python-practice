# Program to find the remainder when a number is divided by z

num1 = int(input("First Number:"))
num2 = int(input("Second Number:"))
Ans_After_Dividation = num1//num2
Remainder = num1 - (num2*Ans_After_Dividation)

print(Remainder)

# Or we can use % symbol for remainder 

num1 = int(input("First Number:"))
num2 = int(input("Second Number:"))
Remainder = num1 % num2
print(Remainder)