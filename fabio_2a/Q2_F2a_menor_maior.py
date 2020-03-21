def main():


    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero: '))

    verificar = menor_maior(n1, n2)

    print(f'O numero {verificar} é o maior e o outro numero é o menor.')


def menor_maior(n1, n2):
    if n1 == n2:
        print('Os dois numeros são iguais.')
    else:
        if n1 < n2:
            return n2
        else:
            return n1

main()
