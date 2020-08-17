def main():

    variavel_n = int(input('Digite um número: '))

    variavel_n

    resultado = 0
    
    variavel_n_print = 0

    while variavel_n > 0:
        resultado += variavel_n
        variavel_n -= 1
        variavel_n_print += 1

    print(f'A soma entre os termos de 1 até {variavel_n_print} é: {resultado}')

main()