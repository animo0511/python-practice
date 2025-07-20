# Break Continue And Pass function

# Break 
for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)

# Continue
for i in range(100):
    if(i == 34):
        continue # Skip this iteration'
    print(i)

# Pass
l = [1, 7, 8]
for item in l:
    pass # Without pass, the program will throw an error
         # It is more like, we will work on it letter