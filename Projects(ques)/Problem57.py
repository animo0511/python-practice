# Same problem 56 for more list of such words to be censored

list_word = ["donkey", "monkey", "bad", "runt"]

# Read the file content
with open("File_For_Donkey_Ques.txt", "r") as f:
    content = f.read()

word_replaced = False

# Replace each word in a case-insensitive manner
for word in list_word:
    if word.lower() in content.lower():  # Check case-insensitively
        # Replace both lowercase and capitalized words
        content = content.replace(word, "#####").replace(word.capitalize(), "#####")
        word_replaced = True  
        print(f"{word} got replaced!")

# Write back the modified content to make the change permanent
if word_replaced:
    with open("File_For_Donkey_Ques.txt", "w") as f:
        f.write(content)  
    print("Censored words replaced successfully!")
else:
    print("No censorable words detected.")

