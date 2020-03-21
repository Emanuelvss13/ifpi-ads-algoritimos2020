def main():
    

    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    n3 = int(input('Digite o 3º número: '))

    verificar = menor_maior(n1, n2, n3)

    print(f'O número {verificar} é o maior e os outros são menores.')


def menor_maior(n1, n2, n3):
    if n1 == n2 and n1 == n3:
        print('Os três numeros são iguais.')
    elif n1 > n2 > n3:
        return n1
    elif n2 > n1 > n3:
        return n2
    else:
        return n3


main()
