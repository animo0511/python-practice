# Exercise 9: Check Palindrome Number

num = 7777777
num_list = list(str(num))
reverse_num = num_list[::-1]

if num_list == reverse_num:
    print(f"original number is {num} \nYes. The given number is a Palindrome.")
else:
    print(f"original number is {num} \nNo. The given number is not a Palindrome.")

