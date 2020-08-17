def main():
    numero = int(input('Digite um número: '))

    fatorial = 1
    numero_print =numero
    
    while numero >= 1:
        fatorial = fatorial * numero
        numero  -= 1

    print(f'O fatorial de {numero_print} é : {fatorial}')


main()