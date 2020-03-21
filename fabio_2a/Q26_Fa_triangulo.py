def main():
    n1 = int(input('Digite o 1º lado: '))
    n2 = int(input('Digite o 2º lado: '))
    n3 = int(input('Digite o 3º lado: '))

    trianguo(n1, n2, n3)

def trianguo(n1, n2, n3):
    if n1 == 0 or n2 == 0 or n3 == 0:
        print('Não existe triângulo com lado 0 :(')
    elif n1 > n2 and  n1 > n3:
        print(f' A hipotenusa é {n1} e os catetos são {n2} e {n3}.')
    elif n2 > n1 and  n2 > n3:
        print(f' A hipotenusa é {n2} e os catetos são {n1} e {n3}.')
    elif n3 > n1 and  n3 > n2:
        print(f' A hipotenusa é {n3} e os catetos são {n1} e {n2}.')
    else:
        print('Esse não é retângulo.')

main()