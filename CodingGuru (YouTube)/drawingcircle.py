import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "white", "blue", "green"]
for x in range(100):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(104)
turtle.done()    