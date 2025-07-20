# Exercise 1: Calculate the multiplication and sum of two numbers

def prod_nums(num1, num2):
    
    product = num1*num2

    if product <= 1000:
        result1 = f"The result is, {product}"
        return result1
    else:
        result2 = f"The result is, {num1+num2}"
        return result2
    

print(prod_nums(20, 30))