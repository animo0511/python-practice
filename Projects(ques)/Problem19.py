#Program to input eight numbers from the user and display all the unique numbers

numbers = set()

num1 = int(input("Enter Number:"))
num2 = int(input("Enter Number:"))
num3 = int(input("Enter Number:"))
num3 = int(input("Enter Number:"))
num4 = int(input("Enter Number:"))
num4 = int(input("Enter Number:"))
num5 = int(input("Enter Number:"))
num6 = int(input("Enter Number:"))
num7 = int(input("Enter Number:"))
num8 = int(input("Enter Number:"))

numbers.update([num1, num2, num3, num4, num5, num6, num7, num8])

print(numbers)