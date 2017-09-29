# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:50:33 2017

@author: Mario Bajenting MarioBajenting@live.com
@author: Cesar Hernandez
"""

import turtle
import math
import random


def draw_right_triangle(name, color, length, degrees, x, y):
    degrees_in_radians = math.radians(degrees)
    name.pencolor(color)

    name.penup()
    name.goto(x, y)

    name.pendown()

    name.forward(-length)
    name.left(degrees)
    name.forward(length / math.cos(degrees_in_radians))
    name.right(90 + degrees)
    name.forward(length * math.tan(degrees_in_radians))

    name.penup()
    name.left(90)


def draw_square(name, color, side1, side2, x, y):
    name.penup()
    name.goto(x, y)
    name.pencolor(color)
    name.fillcolor(color)

# turtle movement
    i = 0
    name.begin_fill()
    while (i < 2):
        name.forward(side1)
        name.left(90)
        name.forward(side2)
        name.left(90)

        i += 1
    name.end_fill()
    name.penup()


def draw_firework(size, x, y):
    firework.penup()
    firework.goto(x, y)
    degrees = 0
    firework.pendown()

    while degrees < 360:
        r = random.random()
        g = random.random()
        b = random.random()

        firework.seth(degrees)
        firework.color(r, g, b)
        firework.pensize(random.randint(1, 5))
        firework.forward(random.randint(0, size))
        firework.goto(x, y)
        degrees += 1

    firework.penup()


def draw_fireworks(n, size, min_x, max_x, min_y, max_y):
    firework.penup()
    firework.pendown()
    while(0 != n):
        x = random.randint(min_x, max_x)
        y = random.randint(min_y, max_y)
        draw_firework(size, x, y)
        n -= 1
    firework.penup()

cesar = turtle.Turtle()
cesar.pensize(1)
cesar.speed(0)
cesar.penup()

firework = turtle.Turtle()
firework.speed(0)
firework.penup()

'''Test Functions'''
# draw_right_triangle(name=cesar, color="red", length=100, degrees=60)
# draw_firework(100, 0, 0)
# draw_square(cesar, "light blue", 1000, 1000, -500, -500)
# draw_fireworks(3, 100, -100, 100, -100, 100)

turtle.exitonclick()
