# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:50:33 2017

@author: Mario Bajenting
@author: Cesar Hernandez
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
    
def draw_square(name, side1, side2, color):
    pass
    name.goto(0, 0)
    name.pencolor(color)
    
    #turtle movement
    i = 0
    while (i < 3):
        name.forward(side1)
        name.left(90)
        name.forward(side2)
        name.left(90)
        i += 1

        #now you need something that 
    
draw_triangle(name = cesar, color = "red", length = 100, degrees = 60)
draw_square (side1 = 5, side2 = 10, color = 'blue')


turtle.exitonclick()