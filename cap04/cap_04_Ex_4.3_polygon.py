import turtle

def polygon(t, n, lenght):
    for i in range(n):
        t.fd(lenght)
        t.lt(360/n)

polygon(turtle.Turtle(), 7, 50)
