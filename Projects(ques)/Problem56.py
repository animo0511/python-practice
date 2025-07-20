# A file contains a word "Donkey" multiple times
# We need to write a program which replace this word with ##### by updating the same files

f = open("File_For_Donkey_Ques.txt")

content = f.read().lower()


if "donkeys" in content:
    change = content.replace("donkeys", "#####")
    with open("File_For_Donkey_Ques.txt", "w") as f:
        f.write(change)   
   
else:
    print("The given doesn't exist in File")