def main():
    numero = int(input('Digite um número: '))

    fatorial = 1
    numero_print =numero
    
    for i in range(numero):
        fatorial = fatorial * numero
        numero  -= 1

    print(f'O fatorial de {numero_print} é : {fatorial}')


main()