# Exercise 7: Return the count of a given substring from a string

def count_of_substr_from_str(og_str:str, sub_str:str):
    count = og_str.count(sub_str)
    print(count)

count_of_substr_from_str("Emma is good developer. Emma is a writer. Emma", "Emma")
