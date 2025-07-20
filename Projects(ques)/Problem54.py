# the game() function in program lets s user play a game
# and returns the score as an integer
# You need to read a file 'Hi-score.txt' 
# which a program to update the HI-score whenever the game() function breaks the Hi-score

# Let a game to generate random number between 1 to 100

import random

def game():
    print("Welcome to game...")
    print("Your score is getting generated...")
    
    num = random.randint(1, 100)
    print(f"Your score is {num}")

    f = open("Hi-score.txt")
    hi_score = f.read()
    f.close()
    if hi_score == "":
        hi_score = "0"

    if num > int(hi_score):
        f = open("Hi-score.txt", "w")
        f.write(str(num))
        f.close()
    else:
        print(f"High Score is: {hi_score}")
game()
