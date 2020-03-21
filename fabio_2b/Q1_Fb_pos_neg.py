def main():
    n = int(input('Digite um número: '))

    pos_neg(n)

def pos_neg(n):
    if n > 0:
        print(f'O número {n} é positivo')
    else:
        print(f'O número {n} é negativo')

main()