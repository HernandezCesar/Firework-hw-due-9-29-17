# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:45:35 2017

@author: Mario Bajenting MarioBajenting@gmail.com
"""

import turtle
import math


def draw_hypotenuse(color, width, degrees):
    zebra.penup()
    zebra.pencolor(color)
    degrees_in_radians = math.radians(degrees)

    zebra.pendown()

    zebra.left(degrees)

    zebra.forward(width / math.cos(degrees_in_radians))

    zebra.penup()
    zebra.seth(0)


#    def spiral(width, angle):
#        zebra.penup()
#
#        space = 10
#        while space < width:
#            draw_hypotenuse("black", space, angle)
#            space += 10


def stripes(color, height, width, angle):
    zebra.penup()
    # draws along base
    x_pos = zebra.xcor()
    y_pos = zebra.ycor()
    space = 10

    while space < width:
        draw_hypotenuse(color, space, angle)
        x_pos -= 10
        zebra.goto(x_pos, y_pos)
        space += 10

    base = zebra.ycor()
    space = 10
    zebra.sety(y_pos + height)
    y_pos = zebra.ycor()

    while y_pos > base:
        draw_hypotenuse(color, space, angle+180)
        y_pos -= 10
        zebra.goto(x_pos, y_pos)
        space += 10


zebra = turtle.Turtle()

stripes("black", 100, 100, 60)

turtle.exitonclick()
