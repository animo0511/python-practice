# Program to mine a log file and find out wheather it contains 'python'

word = 'python'

with open("log.txt", "r") as f:
    content = f.readlines()

for line_num, line in enumerate(content, start=1):
    if word in line:
        print("Present At Line: ") #Tells that it is present or not
        print(line_num) #Tells the number of line hwere it is present
    else:
        continue
if not(word in line):
    print("Absent")
    

