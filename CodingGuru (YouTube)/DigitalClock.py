seconds = 55
minutes = 55
hours = 6
import datetime
import time
from turtle import*
setup()
screen = Screen()
t1 = Turtle()
t1.pencolor("Red")
screen.bgcolor("Black")
while True:
    t1.clear()
    t1.write(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2), font = ("Boulder", 30, "normal"))
    seconds = seconds + 1
    time.sleep(1)
    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
    if minutes == 60:
        minutes = 0
        hours = hours + 1    
