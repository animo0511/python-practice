# Program to print multiplication table of a given number using table

num = int(input("Which num's multiplication do you want:"))


for i in range (0,100000,num):
    if i == 0:
        continue
    if i == num*11:
        break
    print(i)
    


