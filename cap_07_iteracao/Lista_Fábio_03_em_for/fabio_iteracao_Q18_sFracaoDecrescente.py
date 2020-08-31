n = int(input('Digite um número: '))

fracao = 0

for n in range(n, 1-1, -1):

    fracao = fracao + 1 / n
    
    n -= 1


    print(fracao)

print(f'O resultado é: {fracao}')
    