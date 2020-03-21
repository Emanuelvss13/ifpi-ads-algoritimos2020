def main():
   
    n1 = int(input('Digite o primeiro ângulo: '))
    n2 = int(input('Digite o segundo ângulo: '))
    n3 = int(input('Digite o terceiro ângulo: '))

    resultado = triangulo(n1, n2, n3)

    print(resultado)


def triangulo(n1, n2, n3):
    if (n1 + n2 + n3) < 180:
        return 'Esses ângulos não formam um triângulo.'
    
    elif n1 and n2 and n3 == 0:
        return 'Não existe triângulo com ângulo 0 (Zero).'  
    
    else:
        if n1 and n2 and n3 < 90:
            return 'Esses ângulos formam um triângulo acutângulo.'
        elif n1 and n2 and n3 == 90:
            return 'Esses ângulos formam um triângulo retângulo.'
        elif n1 and n2 and n3 > 90:
            return 'Esses ângulos formam um triângulo obtusângulo.'


main()        