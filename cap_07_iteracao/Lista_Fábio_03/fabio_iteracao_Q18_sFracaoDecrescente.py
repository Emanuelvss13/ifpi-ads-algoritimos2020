n = int(input('Digite um número: '))

fracao = 0

while n >= 1:

    fracao = fracao + 1 / n
    
    n -= 1

    print(fracao)

print(f'O resultado é: {fracao}')
    