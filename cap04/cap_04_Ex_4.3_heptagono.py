import turtle

def polygon(t, n, lenght):
    for i in range(n):
        t.fd(lenght)
        t.lt(360/n)
    t.lt(55)
    t.fd(100)
    t.rt(117)
    t.fd(94)
    t.rt(180)
    t.fd(94)
    t.rt(120)
    t.fd(105)
    t.rt(180)
    t.fd(105)
    t.rt(129)
    t.fd(126)
    t.lt(180)
    t.fd(126)
    t.rt(94)
    t.fd(137)
    t.lt(180)
    t.fd(137)
    t.rt(135)
    t.fd(125)

polygon(turtle, 7, 100)