# Program using functions to greatest of three numbers

def greatest(num1, num2, num3):
    num_list = [int(num1), int(num2), int(num3)]
    num_list.sort()
    greatest = num_list[2]
    print("Greatest number between them is: ", greatest)

greatest(23151, 15123, 85151)
