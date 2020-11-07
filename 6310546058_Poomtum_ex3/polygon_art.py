import turtle
import random


def polygon(x, y, size, n, clr):
    turtle.penup()
    turtle.color(clr)
    turtle.fillcolor(clr)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(size)
        turtle.left(360/n)
    turtle.end_fill()


for i in range(100):
    polygon(random.randint(-300, 300), random.randint(-300, 300),
            random.randint(0, 80), random.randint(3, 8), "#a8f7de")
