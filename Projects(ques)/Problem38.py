# Program to find the i of first n natural numbers using while loop

n = int(input("Enter your number: "))

num = 0
i = 1

while i < n+1:
    num += i
    i += 1
print(num)