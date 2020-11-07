import turtle
import random


class Ball:
    def __init__(self, size, x, y, color, screen):
        self.size = size
        self.x = x
        self.y = y
        self.vx = random.randint(1, 0.025* screen.canvas_width)
        self.vy = random.randint(1, 0.025* screen.canvas_width)
        self.color = color

    def draw_circle(self):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_circle(self, screen):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.x += self.vx
        self.y += self.vy

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.x + self.vx) > (screen.canvas_width - screen.ball_radius):
            self.vx = -self.vx
        else:
            self.vx = +self.vx
        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.y + self.vy) > (screen.canvas_height - screen.ball_radius):
            self.vy = -self.vy
        else:
            self.vy = +self.vy


class Screen:
    def __init__(self):
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width
