import turtle
import math

def main(bob, radius):
    t = bob
    r = radius
    circle(t, r)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)




print('                  ***DIAGRAMA DA PILHA***')
print('=========================================================')
print('__main__ "bob"  ----> turtle\n\n         "radius" ----> 100\n\n')
print('=========================================================')
print('__circle__ "t" ----> turtle\n\n           "r ----> 100' )
print('=========================================================')
print('__polygon "t" ----> turtle\n\n          "n" ----> resultado de circumference\n\n          "lenght ----> circumference / "n"')
print('=========================================================')