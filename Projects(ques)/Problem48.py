# Write a recursive function to calculate the sum of first n natural numbers

def sum_of_n_nums(n):
    if n == 0:
        return 0
    return n + sum_of_n_nums(n-1)

print(sum_of_n_nums(15))