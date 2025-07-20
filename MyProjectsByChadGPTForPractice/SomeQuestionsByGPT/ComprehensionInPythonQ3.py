"""From :
values = [10, 15, 20, 25, 30, 35]
Create a set of remainders when each number is divided by 5."""

values = [10, 15, 20, 25, 30, 35]

remainders = {(x % 5) for x in values}

print(remainders)