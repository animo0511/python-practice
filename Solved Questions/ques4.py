# Exercise 5: Check if the first and last number of a list is the same

def first_and_last_is_same(list:list):
    if list[0] == list[len(list)-1]:
        return True
    else:
        return False


print(first_and_last_is_same([75, 65, 35, 75, 30]))