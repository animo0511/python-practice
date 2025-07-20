# num = int(input())

# num_list = list(str(num))
# print(num_list[::-1])

# number = 7536
# print("Given number", number)
# while number > 0:
#     # get the last digit
#     digit = number % 10
#     # remove the last digit and repeat the loop
#     number = number // 10
#     print(digit, end=" ")


n = 7536
l= " "
for i in str(n):
    l = " "+i + l
    print(l)