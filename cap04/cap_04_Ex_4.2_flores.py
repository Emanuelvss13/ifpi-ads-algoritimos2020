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
    for i in range(1):
        t.fd(45)
        t.circle(45 * 1/4)

circle(turtle, 1)
