#Jashan Rai
#Period 1
#recursion_tree.py
#Revised on 3/20/2019
"""This code will create a symmetrical tree using Python turtle graphics"""

import turtle
from random import randint

t = turtle.Turtle(shape="turtle")
t.shape("turtle")
turtle.bgcolor("sky blue")
t.pencolor("brown")
#t.tracer(0)
t.lt(90)

lv = randint(10,20)
l = randint(100,120)
s = randint(10,20)

t.width(lv)

t.penup()
t.bk(l)
t.pendown()
t.fd(l)
t.pencolor("green")
def draw_tree(l, level):
    width = t.width()  # save the current pen width

    t.width(width * 3.0 / 4.0)  # narrow the pen width

    l = 3.0 / 4.0 * l

    t.lt(s)
    t.fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    t.bk(l)
    t.rt(2 * s)
    t.fd(l)
    if level <= lv:
        draw_tree(l, level + 1)
    t.bk(l)
    t.lt(s)
    t.width(width)  # restore the previous pen width

t.speed("fastest")

draw_tree(l, 2)

turtle.done()
