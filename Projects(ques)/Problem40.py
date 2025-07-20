# Program to print the following star pattern 
'''*
   **
   *** for n = 3'''

n = int(input("Enter your Number: "))


for i in range (1, n+1):
    star = i*"*"
    print(star)
    i += 2

    
    

