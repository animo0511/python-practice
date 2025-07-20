# Program to print th following star pattern
'''***
   * *
   *** for n = 3'''

n = int(input("Enter Your Number: "))

for i in range (1, n+1):
    if i == 1 or i == n:
        print("*"*n)
    else:
        print("*" + " "*(n-2) + "*")


