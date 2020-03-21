def main():
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    s = int(input('Digite o número da operação: '))

    operaçao(n1, n2, s)


def operaçao(n1, n2, s):
    if s > 4:
        print('Só exitem 4 operações!')
    elif s == 1:
        print(f'O resultado é: {n1 + n2}.')
    elif s == 2:
        print(f'O resultado é: {n1 - n2}.')
    elif s == 3:
        print(f'O resultado é: {n1 * n2}.')
    else:
        print(f'O resultado é: {n1 / n2}.')

main()
    