def main():
    x1 = int(input('Digite a coordenada do 1º x'))
    y1 = int(input('Digite a coordenada do 2º y'))
    x2 = int(input('Digite a coordenada do 1º y'))
    y2 = int(input('Digite a coordenada do 2º y'))

    ponto(x1, y1, x2, y2)

def ponto(x1, y1, x2, y2):
    if x1 > x2:
        lado = x1 - x2
        altura = y1
        area = lado * altura
   
    elif x2 > x1:
        lado = x2 - x1
        altura = y2
        area = lado * altura

    elif area < 0:
        print('A area não pode ser negativa.')


main()