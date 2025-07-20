import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["burlywood4", "indianred", "green", "blue"]
for x in range (100):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(97)
turtle.done()    