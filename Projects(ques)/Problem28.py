# Program to find wheather a given usernames contains less than 10 characters or not
# Assume, username is not valid if it contains character more than 10

username = input("Enter Your Username:")

count = len(username)

if count>10:
    print("It's contains character more than 10")

else:
    print("It's a valid Username")