def main():
    
    opçao = int(input('Digite 1° número: '))
    num1 = int(input('Digite 2° número: '))
    num2 = int(input('Digite 3° número: '))
    num3 = int(input('Digite 4° número: '))  
    
    resultado = numero(opçao, num1, num2, num3)
    
    print(resultado)


def numero(opçao, num1, num2, num3):
    
    if opçao >= 4 or opçao == 0 :
        return 'No 1º número escreva apenas números de 1 a 3 !'
    elif opçao == 1:
        return f' o valor é {num1}'
    elif opçao == 2:
        return f' o valor é {num2}'
    elif opçao == 3:
        return f' o valor é {num3}'

main()