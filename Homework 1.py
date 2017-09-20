# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:50:33 2017

@author: mario
"""
import turtle
import math

cesar = turtle.Turtle()
cesar.shape("turtle")
cesar.pensize(1)
cesar.speed(0)

def draw_triangle(name,color,length,degrees,x=0,y=0):
    degrees_in_radians = math.radians(degrees)
    name.pencolor(color)
    
    name.penup()
    name.goto(x,y)
        
    name.pendown()
    
    name.forward(-length)
    name.left(degrees)
    name.forward(length/math.cos(degrees_in_radians))
    name.right(90 + degrees)
    name.forward(length * math.tan(degrees_in_radians))
    
    name.penup()
    name.left(90)
    
def square():
    pass
    
draw_triangle(name = cesar, color = "red", length = 100, degrees = 60)
    
turtle.exitonclick()