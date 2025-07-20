# Python function to print multiplication table of a given number

def multi_table(num):
    for i in range(1, 11):
        table = num*i
        print(table)
    return "end"
print(multi_table(10))

# OR Recursive method (Ans by Chatgpt)

def multi_table_recursive(num, i=1):
    if i > 10:  # Base condition (stopping point)
        return
    print(f"{num} × {i} = {num * i}")
    multi_table_recursive(num, i + 1)  # Recursive call

# Example usage
multi_table_recursive(10)
