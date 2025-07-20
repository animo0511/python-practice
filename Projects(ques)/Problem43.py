# Program to print multiplcation tbale of n using for loop in reversed order

n = int(input("Enter Your Number: "))

for i in range (10, 0, -1):
    num = n*i

    table = num
    print(table)

# OR

n = int(input("Enter Your Number: "))

for i in range(1, 11):
    table = n*(11-i)
    print(table)