# Program to find wheather a given number is prime or not

num = int(input("enter the number:"))

if num<2:
    print("I is not a prime number!")

for n in range (2, num):
    if num%n == 0:
        print("It is not a prime number!")
        break
else:
    print("It is a prime number!")



# By Chatgpt

num = int(input("Enter the number: "))

if num < 2:  # Prime numbers start from 2
    print("It is not a prime number!")
else:
    is_prime = True  # Assume it's prime
    for n in range(2, num):
        if num % n == 0:
            is_prime = False  # Found a divisor, so it's not prime
            break  # No need to check further
    
    if is_prime:
        print("It is a prime number!")
    else:
        print("It is not a prime number!")
     
