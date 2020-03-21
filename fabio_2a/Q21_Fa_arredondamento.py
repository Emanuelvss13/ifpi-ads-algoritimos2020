def main():
    n = float(input('Digite um número com uma casa decimal: '))

    arredondamento(n)

def arredondamento(n):
    if n % 1 < 0.5:
        print(f'O número arredondado é: {n - n%1}.')
    else:
        print(f'O número arredondado é: {n + 0.5}.')
main()
    