# Program to print the content of a list using while loops

list = [1, "Hi", 100, True, None, "Mayuresh", False, "Hello"]

i = 0
while i < len(list):
    print(list[i])
    i += 1

# Program to print the content of a list using for loops

for l in range(len(list)): # or we can just write # for i in list:
    print(list[l])

# printing letters of str by using for loop

name = "Mayuresh"

for letters in name:
    print(letters)
