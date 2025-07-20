# continue function is used to skip a word or number from a loop which we dont want
# its 

for x in range (1, 50):
    if x % 4 :
        print(x)
        continue   # it will skip no. which is divisible by 4 from numbers 1 to 50

# and AND or function
# if we want to add a condition we  use 'and'
# if want to use two or more alternate conditions we use 'or'

for x in range (1, 20):
    if x % 4 and x % 3: # in this it will skip the numbers which is divisible by 4 and 3 both
        print(x)        # like 12 , 
        continue  

for x in range (1, 20):
    if x % 4 or x % 3: # it will skip numbers which is divisible by 4 and 3 indivusualy 
        print(x)       # like 3, 4, 6, 8, 9, 12, 
        continue  
  