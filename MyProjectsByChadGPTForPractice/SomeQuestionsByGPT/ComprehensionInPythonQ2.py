'''From this list:
numbers = [3, 8, 6, 7, 10, 15, 22]
Create a new list with even numbers only using list comprehension.'''

numbers = [3, 8, 6, 7, 10, 15, 22]

even = [x for x in numbers if x % 2 == 0]

print(even)