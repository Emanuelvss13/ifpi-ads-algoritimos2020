def main():
    variavel_n = int(input('Digite quantos números devem ter: '))
    
    contador = 0

    numb_1 = 0
    numb_2 = 1

    if variavel_n < 2:
        print('O número deve ser maior ou igual a 2!')
    else:
        while contador < variavel_n:
                numb_sum = numb_1 + numb_2 
                numb_1 = numb_2 
                numb_2 = numb_sum 
                print(numb_2)
                contador += 1


main()