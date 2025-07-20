# Program to print the following star pattern 
'''  *
    ***
   ***** for n = 3'''

n = int(input("Enter Your Number: "))

num = -1

for i in range(1, n+1):
    num += 2
    spaces = " " * (n - i) # It is suggested by Jr.ChatGpt
    star = num*"*"
    print(spaces + star)



