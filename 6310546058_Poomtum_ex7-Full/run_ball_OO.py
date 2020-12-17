from ball_OO import *
import turtle
import random
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
turtle.colormode(255)
screen = Screen()
numb_all = int(input("Number of balls to simulate: "))
ball_list = [Ball(screen.ball_radius,
                random.randint(-1 * screen.canvas_width + screen.ball_radius, screen.canvas_width - screen.ball_radius),
                random.randint(-1 * screen.canvas_width + screen.ball_radius, screen.canvas_width - screen.ball_radius),
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), screen) for i in
           range(numb_all)]
while True:
    turtle.clear()
    for i in ball_list:
        i.draw_circle()
        i.move_circle(screen)
    turtle.update()