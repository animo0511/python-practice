import turtle
t = turtle.Pen()
turtle.speed(20)
num_of_circles = int(turtle.numinput("No. of Circles", "How many circles do you want?"))
for x in range(num_of_circles):
    t.circle(100)
    t.left(360/num_of_circles)
turtle.done()    