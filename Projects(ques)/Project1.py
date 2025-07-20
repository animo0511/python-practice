# PROJECT1 :- SNAKE, WATER, GUN GAME
# I WANT TO CONVERT IT IN A ROCK, PAPER, SCISSORS GAME

''''
now Let
Rock = -1
Paper = 1
Scissors = 0'''
import random

options = ["Rock", "Paper", "Scissors"]

comp = random.choice(options)

our_choice = input("Rock, Paper OR Scissors? : ")

if comp == our_choice:
    print(f"Computers choice is {comp}")
    print(f"Your choice is {our_choice}")
    print("It's a TIE")
elif (comp == "Rock" and our_choice == "Paper") or (comp == "Paper" and our_choice == "Scissors") or (comp == "Scissors" and our_choice == "Rock"):
    print(f"Computers choice is {comp}")
    print(f"Your choice is {our_choice}")
    print("You Win !")
else:
    print(f"Computers choice is {comp}")
    print(f"Your choice is {our_choice}")
    print("You Loose!")
    

