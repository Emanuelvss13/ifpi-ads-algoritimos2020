import turtle
from math import pi

def arc(a):
    circle(turtle, a)
    polygon(turtle, 720, a )

def circle(t, a):
    polygon(turtle, 720, a )


def polygon(t, n, a):
    for i in range(a):
        t.fd(1)
        t.lt(360/n)

arc(180)