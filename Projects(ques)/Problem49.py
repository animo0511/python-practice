# Python function to print first n lines of the following pattern
'''***
   **
   *     for n = 3'''


def star_pattern(n):
    for i in range (n, 0, -1):
        star = i*"*"
        print(star)

star_pattern(10)

#OR by CodeWithHarry

def pattern(n):
    if n == 0:
        return
    print("*"*n)
    pattern(n-1)