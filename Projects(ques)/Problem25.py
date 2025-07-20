# Program to find the greater of four numbers entered by the user 

num1 = int(input("Enter Number:"))
num2 = int(input("Enter Number:"))
num3 = int(input("Enter Number:"))
num4 = int(input("Enter Number:"))

if num1>num2 and num1>num3 and num1>num4:
    print("The greatest number is:", num1)

elif num2>num1 and num2>num3 and num2>num4: 
    print("The greatest number is:", num2)

elif num3>num1 and num3>num2 and num3>num4:
    print("The greatest number is:", num2)

elif num4>num1 and num4>num2 and num4>num2:
    print("The greatest number is:", num4)

    

