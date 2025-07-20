# Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# MY APPROACH
for x in range (5):
    if x==0:
        x = "1"
    elif x==1:
        x = (x+1)*"2"
    elif x==2:
        x = (x+1)*"3"
    elif x==3:
        x = (x+1)*"4"
    elif x==4:
        x = (x+1)*"5"
    print(x)

# ANSWER BY QUESTION GIVEN
for num in range(6):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")

    