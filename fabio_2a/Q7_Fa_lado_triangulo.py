def main():
    
    n1 = int(input('Digite o tamanho do 1º lado do triângulo: '))
    n2 = int(input('Digite o tamanho do 2º lado do triângulo: '))
    n3 = int(input('Digite o tamanho do 3º lado do triângulo: '))

    resultado = lado_triangulo(n1, n2, n3)

    print(resultado)

def lado_triangulo(n1, n2, n3):
    if n1 and n2 and n3 == 0:
        return 'Não exite triângulo com tamanho 0 (Zero).'
    
    elif (n1 + n2) < n3:
        return 'a soma de dois lados não pode ser menor que o terceiro lado.'
    
    elif (n2 + n3) < n1:
        return 'a soma de dois lados não pode ser menor que o terceiro lado.'
    
    elif (n1 + n3) < n2:
        return 'a soma de dois lados não pode ser menor que o terceiro lado.'
    
    else:
        if n1 == n2 == n3:
            return 'Esse triângulo é equilátero.'
        elif n1 != n2 != n3:
            return 'Esse triângulo é escaleno.'
        else:
            return 'Esse triângulo é isósceles. '


main()

