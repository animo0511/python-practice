"""1) Write a Python program to calculates the area of a right-angled triangle
where base and height are given.
Requirements:
a) Prompt the user to input the base and height of a triangle.
b) Ensure the inputs are numeric and non-negative. If the user enters an
invalid input (e.g., a negative number or non-numeric input), display an
appropriate error message.
c) Calculate the area of the triangle using valid inputs.
d) Display the result formatted to 2 decimal places.

Sample Input/Output:
Enter base of the triangle: 5
Enter height of the triangle: 10
Area of the triangle is: 25.00"""

# ANS:- 

# We handling errors hear so 

try:
    # Taking inputs from user 
    base = float(input("Enter base of the triangle: "))
    height = float(input("Enter height of the triangle: "))

    # Handling negative inputs 
    assert base >= 0, "base cannot be negative."
    assert height >= 0, "height cannot be negative."

    # Calculations 
    area = 1/2 * base * height

    # Diplay OutPut 
    print(f"Area of the triangle is: {area:.2f}")

except AssertionError as a:
    print("Input Error:", a)
except ValueError:
    print("Input Error: please enter a numeric value.")




"""2) Write a Python program to calculate the hypotenuse of a right-angled
triangle where the two perpendicular sides are given.
Requirements:
a) Prompt the user to input the lengths of the two perpendicular sides
(side A and side B) of the triangle.
b) Ensure the inputs are numeric and non-negative. If the user enters an
invalid input (e.g., a negative number or non-numeric value), display an
appropriate error message.
c) Calculate the hypotenuse using the Pythagorean theorem.
d) Display the result formatted to 2 decimal places.

Sample Input/Output:
Enter length of side A: 3
Enter length of side B: 4
Hypotenuse of the triangle is: 5.00"""

# ANS:- 

# We are handling error here 
try:
    # Taking inputs 
    sideA = float(input("Enter length of side A: "))
    sideB = float(input("Enter length of sode B: "))

    # Making assert coditions for negative inputs 
    assert sideA >= 0 and sideB >= 0, "side of triangle cannot be negative"

    # Calculations 
    hypotenuse = ((sideA**2) + (sideB**2))**0.5

    # Display OutPut 
    print(f"Hypotenuse of the triangle is {hypotenuse:.2f}")

except AssertionError as a:
    print("Input Error:", a)
except ValueError:
    print("Input Error: please enter a numeric value.")




"""3) Write a Python program to calculate the volume of a cylinder where
radius and height are given.
Requirements:
a) Prompt the user to input the radius and height of the cylinder.
b) Ensure the inputs are numeric and non-negative. If the user enters an
invalid input (e.g., a negative number or non-numeric value), display an
appropriate error message.
c) Calculate the volume of the cylinder using valid inputs.
d) Display the result formatted to 2 decimal places.

Sample Input/Output:
Enter radius of the cylinder: 5
Enter height of the cylinder: 10
Volume of the cylinder is: 785.40"""

# ANS:-
 
import math
# Handling Errors 
try:
    # Taking Input
    radii = float(input("Enter radius of the cylinder: "))
    height = float(input("Enter height of the cylinder: "))

    # Handling negative value error
    assert radii >= 0, "radius of cylinder cannot be negative."
    assert height >=0, "height of the cylinder cannot be negative."

    # Calculations
    volume = math.pi * (radii**2) * height

    # Display OutPut 
    print(f"Volume of the cylinder is {volume:.2f}")

except AssertionError as a:
    print("Input Error:", a)
except ValueError:
    print("Input Error: please enter a numeric value.")




"""4) Write a Python program to determine how many complete dozens are in a
given number of items and what the remainder is.
Requirements:
a) Prompt the user to input the total number of items.
b) Ensure the input is a non-negative numeric value. If the user enters
an invalid input (e.g., a negative number or non-numeric value), display
an appropriate error message.
c) Calculate how many complete dozens (i.e., groups of 12 items) are
present in the given number, and also compute the remainder.
d) Display the result clearly indicating the number of dozens and the
remainder.

Sample Input/Output:
Enter the total number of items: 157
Complete dozens: 13
Remaining items: 1"""

# ANS:- 

# Handling Error 
try:
    # Input by user 
    total_num = int(input("Enter the total number of items: "))

    # Error Handling 
    assert total_num >= 0, "please enter a non-negative value."

    # Calculations for Dozens and Ramaining item 
    complete_dozen = total_num//12
    ramaining = total_num % 12

    # Display OutPut
    print(f"Complete dozens: {complete_dozen}")
    print(f"Ramaining items: {ramaining}")

except AssertionError as a:
    print("Input Error:", a)
except ValueError:
    print("Input Error: please enter a numeric value.")