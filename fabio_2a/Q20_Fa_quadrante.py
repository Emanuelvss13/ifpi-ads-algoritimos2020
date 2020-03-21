def main():
    angulo = int(input('Digite um ângulo: '))

    quadrante(angulo)


def  quadrante(angulo):
    if angulo < 0 or angulo > 360:
        print('Digite apenas ângulo entre 0° a 360° !') 
    elif angulo > 0 and angulo <= 90:
        print('Ele pertence ao 1º quadrante.')
    elif angulo > 90 and angulo <= 180:
        print('Ele pertence ao 2º quadrante.')
    elif angulo > 180 and angulo <= 270:
        print('Ele pertence ao 3º quadrante.')
    else:
        print('Ele pertence ao 4º quadrante.')

main()