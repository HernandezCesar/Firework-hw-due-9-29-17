# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 18:48:11 2017

@author: Cesar Hernandez
"""
import random
import turtle


def draw_rectangle(color, width, height):
    skyline.penup()
    skyline.pencolor(color)
    skyline.fillcolor(color)

    i = 0
    skyline.begin_fill()
    while (i < 2):
        skyline.forward(width)
        skyline.left(90)
        skyline.forward(height)
        skyline.left(90)
        i += 1
    skyline.end_fill()
    skyline.penup()


def draw_skyline(color):
    skyline.penup()
    skyline.setx(-window_width / 2)
    skyline.sety(-window_height / 2)
    skyline.pencolor(color)
    skyline.pendown()

    skyline_width = 0
    while skyline_width < window_width:
        width = random.randint(10, int(window_width / 10))
        height = random.randint(100, int(window_height / 2))
        draw_rectangle(color, width, height)
        skyline.forward(width)
        skyline_width += width

window_height = random.randint(500, 750)
window_width = random.randint(500, 750)
turtle.setup(window_width, window_height)

skyline = turtle.Turtle()
skyline.pensize(1)
skyline.speed(0)
skyline.penup()


draw_skyline("black")
# draw_rectangle("black", 10, 20)


turtle.exitonclick()
