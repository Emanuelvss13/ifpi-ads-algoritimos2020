def main():

    a = int(input('Digite um número de dois digitos: '))
    
    resultado = dois_digitos(a)

    print(f'==================RESULTADO=================\n{resultado}')

def dois_digitos(a):
    if (a // 10) != (a % 10):
        return 'o algarimo da dezena é diferente do da unidade'
    
    else:
        return 'os algarismos são iguais'

main()