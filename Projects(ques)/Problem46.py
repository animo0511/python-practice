# Program using function to convert Celsis to Fahrenheit

def convert_C_to_F (num):
    F = (num*1.8)+32
    round(F, 2) # Use to round of the answer to 2 decimals
    print(f"It will be {F} °F  ")

convert_C_to_F(30)    