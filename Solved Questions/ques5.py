# Exercise 6: Display numbers divisible by 5 from a list

def is_element_div_by_five(list):
    for x in range(len(list)):
            if list[x]%5 == 0:
                print(list[x])


is_element_div_by_five([10, 20, 33, 46, 55])