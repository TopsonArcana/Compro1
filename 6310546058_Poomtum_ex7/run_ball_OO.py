from ball_OO import *
import turtle
import random

turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
turtle.colormode(255)
screen = Screen()
numball = int(input("Number of balls to simulate: "))
ballist = [Ball(screen.ball_radius,
                random.randint(-1 * screen.canvas_width + screen.ball_radius, screen.canvas_width - screen.ball_radius),
                random.randint(-1 * screen.canvas_width + screen.ball_radius, screen.canvas_width - screen.ball_radius),
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                screen)
           for i in range(numball)]

while True:
    turtle.clear()
    for ball in ballist:
        ball.draw_circle()
        ball.move_circle(screen)
    turtle.update()
