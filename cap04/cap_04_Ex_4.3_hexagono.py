import turtle

def polygon(t, n, lenght):
    for i in range(n):
        t.fd(lenght)
        t.lt(360/n)
    t.lt(45)
    t.fd(80)
    t.rt(95)
    t.fd(72)
    t.rt(180)
    t.fd(72)
    t.rt(112)
    t.fd(98)
    t.rt(180)
    t.fd(98)
    t.rt(115)
    t.fd(150)
        
        
        
polygon(turtle, 6, 100)