def main():
    variavel_n = int(input('Digite um número: '))
    lista_de_n = int(input('Digite um número essa lista deve ter: '))

    comeco = 0
    soma = 0
    media = 0

    for i in range(comeco, lista_de_n):
        soma += variavel_n
        variavel_n += 1
        comeco += 1
    
    media = soma / lista_de_n
    
    print(f'A soma dos números é: {soma}, e a média é: {media} essa lista tem {lista_de_n} números.')


main()