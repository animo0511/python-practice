# Program to open three files 1.txt, 2.txt and 3.txt if any these files are not present without existing the program must nr printd prompting the same
try:
    with open("1.txt", "r") as f1:
        print(f1.read())
except Exception as e:
    print(e)

try:
    with open("2.txt", "r") as f2:
        print(f2.read())
except Exception as e:
    print(e)

try:
    with open("3.txt", "r") as f3:
        print(f3.read())
except Exception as e:
    print(e)

print("Thank You !")