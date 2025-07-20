# using break fiunction 
# i want to make a vending machine code, in which we set a limit for packets in it and add a loop 
# in it we break it if user ask for more packets than we have

a = 4
x = int(input("How chips packets do you want ?"))
i = 1
while i<=x:
    if i>a:
        print("We are out of stock !")
        break
    i = i + 1
    print("Packet")
print("Thank you purchasing !")      
