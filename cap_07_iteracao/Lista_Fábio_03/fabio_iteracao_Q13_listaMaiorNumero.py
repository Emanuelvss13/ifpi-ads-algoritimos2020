def main():
    variavel_n = int(input('Digite um número: '))
    lista_de_n = int(input('Digite quantos números essa lista deve ter: '))

    comeco = 0
    soma = 0


    while lista_de_n >= comeco:
        soma += variavel_n
        variavel_n += 1
        comeco += 1


    
    print(f'O maior número é: {variavel_n - 1}')


main()