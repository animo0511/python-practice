"""Q.1) Write a Python program that demonstrates the use of print statements with
different types of quotes.
Requirements:
• Use the exact print statements provided in the example
• Explain the difference between single quotes (') and double quotes (")
• Show how to handle quotes within quotes
• Run the program and observe the output"""

# ANS:- 

print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print("Python", "Programming", "Lab")
print("Age: ", 25)
print(10, 20, 30)
print('Yay! Printing.')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')




"""Q.2) Write a Python program that demonstrates advanced print() function
usage. Your code should:
• Print multiple values with a custom ending instead of a newline
• Print multiple values with a custom separator between them
• Combine both custom separator and ending in a single print
statement
• Show how these parameters affect the output formatting"""

# ANS:-

# Python Program: Use of Separator and End
# Parameters in print() Function
# Program demonstrating the use of 'sep' and 'end'
# parameters in print() function  
print("=" * 50)
print("DEMONSTRATION OF sep AND end PARAMETERS")
print("=" * 50)

# Example 1: Using custom 'end' parameter
print("\n1. Using custom 'end' parameter:")
print("Code: print('Hello', 'World!', end='####')")
print("Hello", "World!", end='####')

# Example 2: Using custom 'sep' parameter
print("\n\n2. Using custom 'sep' parameter:")
print("Code: print('Bye', 'World!', sep='$$')")
print("Bye", "World!", sep='$$')

# Example 3: Using both 'sep' and 'end' parameters
print("\n\n3. Using both 'sep' and 'end' parameters:")
print("Code: print('With sep', 'and end', sep=' ', end='.\\n')")
print("With sep", "and end", sep=' ', end='.\n')
# Additional examples for better understanding
print("\n" + "=" * 50)
print("ADDITIONAL EXAMPLES FOR BETTER UNDERSTANDING")
print("=" * 50)
# Example 4: Default behavior (for comparison)
print("\n4. Default print() behavior:")
print("Code: print('Python', 'Programming', 'Language')")
print("Python", "Programming", "Language")
# Example 5: Different separators
print("\n5. Different separators:")
print("Code: print('Apple', 'Banana', 'Cherry', sep=' | ')")
print("Apple", "Banana", "Cherry", sep=' | ')
print("Code: print('One', 'Two', 'Three', sep='-')")
print("One", "Two", "Three", sep='-')
# Example 6: Different end characters
print("\n6. Different end characters:")
print("Code: print('Loading', end='... ')")
print("Loading", end='... ')
print("Code: print('Done!')")
print("Done!")
# Example 7: Empty separator
print("\n7. Empty separator:")
print("Code: print('No', 'Space', 'Between', sep='')")
print("No", "Space", "Between", sep='')
# Example 8: Multiple custom parameters
print("\n8. Multiple custom parameters:")
print("Code: print('Start', 'Middle', 'End', sep=' -> ', end=' [Complete]\\n')")
print("Start", "Middle", "End", sep=' -> ',
end='[Complete]\n')
print("\n" + "=" * 50)
print("EXPLANATION:")
print("=" * 50)
print("* sep: Defines what to print between multiple values (default is space)")
print("* end: Defines what to print at the end of the line (default is newline \\n)")
print("* Both parameters help control the formatting of output")
print("=" * 50)




"""Q.3) Write a Python program that asks for a user's name and year of birth, then
displays their age.
Requirements:
• Prompt the user to enter their name
• Prompt the user to enter their year of birth
• Calculate and display the user's age
• Format the output as shown in the sample

Sample Output:
Enter your name: Guido van Rossum
Enter your year of birth: 1956
Hey Guido van Rossum you are 67 years old!"""

# ANS:- 

# Taking user output 
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))

# Calculations
current_year = 2025 #This is a current running year 
age = current_year - year_of_birth

# Diplay OutPut
print(f"Hey {name} you are {age} years old!")




"""Q.4) Write a Python program to calculate compound interest using the formula
A = P (1 + r/n)^nt
where P is Principal amount (initial investment), r is annual
interest rate (as a decimal), n is number of times interest is compounded per
year, t is number of years and A is final amount.
Requirements:
• Take user input for P, r, n and t
• Calculate and display the final amount and compound interest
earned.
• Format the output to 2 decimal places.

Sample Input/Output:
Enter principal amount: 1000
Enter annual interest rate (%): 5
Enter compounding frequency per year: 12
Enter number of years: 2
Final Amount: Rs. 1104.89
# Compound Interest Earned: Rs. 104.89"""

# ANS:-

# Taking input from user 
principal_amount = float(input("Enter principal amount: "))
annual_interest = float(input("Enter annual interest rate (%): "))
n = int(input("Enter compounding frequency per year: "))
t = float(input("Enter number of years: "))

# Rate
rate = annual_interest/100

# Calculating Final Amount and Compound Interest Earned 
final_amount = principal_amount * ((1 + (rate/n))** (n*t))
compound_interest = final_amount - principal_amount

# Diplay OutPut
print(f"Final Amount: {final_amount:,.2f}")
print(f"Compound Interest Earned: {compound_interest:,.2f}")




"""Q.5) Write a Python program that calculates the area of a circle.
Requirements:
• Take user input for radius.
• Calculate the area using the formula π × r
2
.
• Format the output to 2 decimal places.
# • Handle invalid input (negative numbers or non-numeric values)

Sample Input/Output:
Enter radius: 5.5
Radius: 5.5, Area: 95.03"""

# ANS:- 

# We are going to solve this ques with handlig errors
try:
    pi = 22/7 # Defined value of pi 
    radii = float(input("Enter radius: ")) # Taking user input
    assert radii >= 0, "radius can't be negative." # Making condition to input only positive value
    area = pi * (radii*radii) # Calculation
    print(f"Radius: {radii}, Area: {area:.2f}") # Diplay OutPut 

except AssertionError as a:
    print("Input Error: ", a)
except ValueError:
    print("Input Error: please enter numeric value")

# NOTE: We can use math module to export pi value for this ques, i'll be using that for further questions 







