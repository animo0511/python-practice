# Here is the Coding Quiz Program 
# It consist of one word ans ques

def quiz():

    score = 0

    q1 = input("1.What keyword is used to define a function in Python? ")
    if q1 == "def":
        print("CORRECT")
        score += 1

    q2 = input("2.What data type is returned by input() function? ")
    if q2 == "str" or q2.lower() == "string":
        print("CORRECT")
        score += 1

    q3 = input("3.Which keyword is used to start a loop that runs while a condition is true? ")
    if q3.lower() == "while":
        print("CORRECT")
        score += 1

    q4 = input("4.What data structure is mutable: list or tuple? ")
    if q4.lower() == "list":
        print("CORRECT")
        score += 1

    q5 = input("5.What is the output type of len() function? ")
    if q5 == "int" or q5.lower() == "integer":
        print("CORRECT")
        score += 1

    q6 = input("6.Which keyword is used to handle exceptions? ")
    if q6 == "except":
        print("CORRECT")
        score += 1

    q7 = input("7.What operator is used for exponentiation in Python? ")
    if q7 == "**":
        print("CORRECT")
        score += 1

    q8 = input("8.Which data type only has True or False values? ")
    if q8.lower() == "bool" or q8.lower() == "boolean":
        print("CORRECT")
        score += 1

    q9 = input("9.What keyword is used to exit a function and send back a result? ")
    if q9 == "return":
        print("CORRECT")
        score += 1

    q10 = input("10.What is the default value of end in the print() function? ")
    if q10 == "\\n":
        print("CORRECT")
        score += 1
    
    print(f"Your Final Score is {score}")


quiz()