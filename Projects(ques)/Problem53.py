# Program to read the text from a given file 'poems.txt' and find out wheather it contains the world 'Twinkle'

f = open("poems.txt", "r")

words_in_file = f.read().lower()
word = "twinkle"

if word in words_in_file:
    print(f"{word} exists in file")
else:
    print(f"{word} doesn't exist in file")

f.close()

### ORRRR





