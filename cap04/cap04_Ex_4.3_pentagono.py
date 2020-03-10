import turtle

def polygon(t, n, lenght):
    for i in range(n):
        t.fd(lenght)
        t.lt(360/n)
    t.lt(45)
    t.fd(81)
    t.rt(98)
    t.fd(72)
    t.lt(180)
    t.fd(72)
    t.rt(99)
    t.fd(81)
    t.lt(180)
    t.fd(81)
    t.rt(50)
    t.fd(97)
    t.lt(180)
    t.fd(97)
    t.lt(115)
    t.fd(100)

polygon(turtle.Turtle(), 5, 100)
