def main():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))

    backend(n1, n2)


def backend(n1, n2):
    if n1 == 0 or n2 == 0:
        print('Nenuhm dos números pode ser 0 (zero)!')
    elif n1 % n2 == 1:
        print (f'A soma das variaveis com o resto é: {(n1 + n2) + (n1 % n2)}')
    
    elif n1 % n2 == 2:
        if n1 % 10 == 0 or n1 % 10 == 2 or n1 % 10 == 4 or n1 % 10 == 6 or n1 % 10 == 8:
            print (f'O {n1} é par', end= ' ')
        if n2 % 10 == 0 or n2 % 10 == 2 or n2 % 10 == 4 or n2 % 10 == 6 or n2 % 10 == 8:
            print(f'e o {n2} também é par.')
        else:
            print(f'O número {n1} é impar', end= ' ')     
            print(f'e o número {n2} também é impar.')
    
    elif n1 % n2 == 3:
        soma = n1 + n2
        resultado = soma * n1
        print(f'A multiplicaçao da soma pelo número um é: {resultado}')
    
    elif n1 % n2 == 4:
        soma = n1 + n2
        resultado = soma / n2
        print(f'A divisão da soma pelo segundo número é: {resultado}')

    else:
        q1 = n1 ** 2
        q2 = n2 ** 2
        print(f'O quadrado do 1º número é {q1} e do 2º é {q2}')


main()