# Program to find out whether a file is identical & mathches the content of another file

with open("this.txt", "r") as f1:
    content1 = f1.read()
with open("copy.txt", "r") as f2:
    content2 = f2.read()

if content1 == content2: # compare the contents in the files
    print("Both files are identical !")
else:
    print("Both files are not identical !")
