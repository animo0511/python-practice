#We are going write a program that generates a random number and asks the user to guess it
# If the player's guess is higher than the actual number, the program displays "Lower number please". Similarly, if the user's guess is too low, the program prints "higher number please" When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number
# Hint:- Use the random module

import random

n = random.randint(1, 10)
a = -1
guesses = 0
while (a != n):
    guesses += 1
    a = int(input("Guess the number:- "))
    if (a>n):
        print("Lower number please")
    else:
        print("Higher number please")

print(f"You have guesssed the number {n} correctly in {guesses} attempts !")

