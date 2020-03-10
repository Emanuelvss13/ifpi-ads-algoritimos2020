import turtle
from math import pi

def circle(t, r):
    circun = (2 * pi) * r
    n = int(circun / 3) + 1
    polygon(turtle, n, 1 )


def polygon(t, n, lenght):
    angle = 360.0/n
    for i in range(n):
        t.fd(lenght)
        t.lt(angle)

circle(turtle, 100)