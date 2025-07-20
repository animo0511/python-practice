import turtle
t = turtle.Turtle()
t.pensize(7)
t.pencolor("Red")
number_sides = 10
side_length = 80
angle = 360.0/number_sides
for i in range(number_sides):
    t.begin_fill()
    t.forward(side_length)
    t.right(angle)
    t.end_fill()
turtle.done()    