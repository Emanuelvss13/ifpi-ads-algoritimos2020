n = int(input('Digite um número: '))

denominador = 1

fracao = 0

while n >= denominador:

    fracao = fracao + 1 / denominador
    
    denominador += 1

    print(fracao)

print(f'O resultado é: {fracao}')
    