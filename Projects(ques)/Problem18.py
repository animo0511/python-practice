# Program to create a dictionary of Hindi eords with as their English translation
# Provide user with options to look it up

words = {
    "Namaste" : "Hello",
    "Ha" : "Yes",
    "Nahi" : "No",
    "Krupaya" : "Please",
    "Dhanyavad" : "Thank You"
}
to_find = input("Enter a Word:")

meaning = words.get(to_find)
print(meaning)