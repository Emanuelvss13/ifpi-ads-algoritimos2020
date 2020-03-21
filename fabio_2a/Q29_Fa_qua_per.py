def main():
    n = int(input('Digite um número de 4 digitos: '))

    qua_per(n)

def qua_per(n):
    d2 = n % 100
    e0 =  (n * 1/100)
    e1 = (n * 1/100)%1
    e2 = e0 - e1
    qp = d2 + e2
    sqrt = n ** (1/2)
    if sqrt == qp:
        print('Esse número é um quadrado perfeito.')
    else:
        print('Esse número não é um quadrado perfeito.')

main()