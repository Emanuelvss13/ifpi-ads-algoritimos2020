import turtle

def espiral(a):
    t = turtle.Turtle()
    distancia = a
    for i in range(100):
        t.speed(10)
        t.fd(distancia)
        t.lt(90)
        distancia = distancia + 10


espiral(10)