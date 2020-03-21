def main():
    n = int(input('Digite um número de 4 digitos: '))

    qwerty(n)

def qwerty(n):
    d2 = n % 100
    e0 =  (n * 1/100)
    e1 = (n * 1/100)%1
    e2 = e0 - e1
    qp = (d2 + e2) ** 2
    if n == qp:
        print(f'A soma dos termos é {d2 + e2} e o quadrado é {qp}.')
    else:
        print('O quadrado da soma dos digitos não é igual ao número :(')

main()