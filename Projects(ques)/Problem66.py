# cerate a class with a class attributes a; create an object from it and set 'a'\
# Directly using objet.a = 0. Does this change the class attribute

class Demo:
    a = 4

o = Demo()
print(o.a)# Prints the class attributes because instance attribute is not present

o.a = 0 # Instance attribute is set
print(o.a) # Prints the instance attribute because instance attribute is present

print(Demo.a) # By printing this we can see that, class attribute doesn't change