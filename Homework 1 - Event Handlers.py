# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 18:34:30 2017

@author: Mario Bajenting MarioBajenting@gmail.com
"""
import turtle
import random

turtle.setup(random.randint(250, 750), random.randint(250, 750))
wn = turtle.Screen()
blind = turtle.Turtle()


def crawl():
    i = 0
    blind.pensize(1)
    while i < 100:
        r = random.random()
        g = random.random()
        b = random.random()
        blind.color(r, g, b)
        blind.seth(random.randint(0, 360))
        blind.forward(10)
        i += 1


def firework():
    x = blind.xcor()
    y = blind.ycor()
    degrees = 0
    while degrees < 360:

        r = random.random()
        g = random.random()
        b = random.random()

        blind.seth(degrees)
        blind.color(r, g, b)
        blind.goto(x, y)
        blind.pensize(random.randint(1, 5))
        blind.forward(random.randint(0, 100))
        degrees += 1

wn.onkey(crawl, "c")
wn.onkey(firework, "f")

blind.speed(0)

wn.listen()
wn.mainloop()
