# Exercise 4: Remove first n characters from a string

def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print(remove_chars("MAYURESH", 5))
