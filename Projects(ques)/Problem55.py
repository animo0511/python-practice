# Program to generate multiplication tables from 2 to 20
# and Write it to the different files
# Place these files in a folder for a 13- year old
import os

def tables(num):
    full_table = ""
    for i in range (1, 11):
        full_table +=  f"{num}x{i}={i*num}\n"
    return full_table

os.makedirs("Tables", exist_ok=True)

for n in range(2, 21):
    with open(f"Tables/table{n}.txt", "w") as f:
       f.write(str(tables(n)))
       f.write("Related to Problem 55")

    
