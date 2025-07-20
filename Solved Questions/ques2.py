# Exercise 3: Print characters from a string that are present at an even index number

def char_at_even_index(string):
    char_at_index = []
    for x in range (len(string)):
        if x%2 == 0:
            char_at_index.append(string[x])
    
    return "\n".join(char_at_index)
    


print(char_at_even_index("mayuresh"))         