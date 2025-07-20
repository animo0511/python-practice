# Program which finds out wheather a given is present in a names_list or not
# Let names_list = ["Ramesh", "Raj", "Sameer", "Rani", "Mayur", "Tanmay", "Harsh"]

names_list = ["Ramesh", "Raj", "Sameer", "Rani", "Mayur", "Tanmay", "Harsh"]

name = input("Enter your name:")

if names_list.count(name) == 1:
    print("You are in the list !")

else:
    print("You are not in the list !")    

# OR according to chatgpt

if name in names_list:
    print("You are in the list !")

else:
    print("You are not in the list !")    