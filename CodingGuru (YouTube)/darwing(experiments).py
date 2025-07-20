import turtle
t = turtle.Pen()
colors = ["red", "black", "green", "orange", "blue"]
for x in range (100):
    t.forward(x)
    t.pencolor(colors[x%5])
    t.left(120)
    t.forward(x)
    t.right(20)
turtle.done()    