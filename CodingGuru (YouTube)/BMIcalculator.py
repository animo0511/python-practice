import turtle
your_weight = turtle.numinput("Your Weight","What is your weight?")
your_height = turtle.numinput("Your Height","What is your height?")
BMI = your_weight/(your_height/100)**2
print("This is your BMI calculation -", BMI)