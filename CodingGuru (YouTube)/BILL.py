#Making BILL like supermarket
import turtle
juice = turtle.numinput("NO. of juice buyed", "Hoe many juice buyed?")
coffee = turtle.numinput("NO. of coffee buyed", "How many coffee buyed?")
green_tea = turtle.numinput("NO. of green tea", "How many green tea buyed?")
tea = turtle.numinput("NO. of tea", "How many tea buyed?")
donuts = turtle.numinput("NO. of donuts", "How many donuts buyed?")
cupcake = turtle.numinput("NO. of cupcake", "How many cupcake buyed?")
price_juice = 30
price_coffee = 50
price_green_tea = 50
price__tea = 20
price__donuts = 70
price__cupcake = 50
BILL = juice*price_juice + coffee*price_coffee + green_tea*price_green_tea + tea*price__tea + donuts*price__donuts + cupcake*price__cupcake
GST = 0.6
GST_price =  BILL*GST
Total_BILL = BILL + GST_price
print("Your BILL is. -", BILL)
print("Total GST of. -", GST, ("%"), ("then your total GST is"), GST_price)
print("YOUR Total BILL is. -", Total_BILL)