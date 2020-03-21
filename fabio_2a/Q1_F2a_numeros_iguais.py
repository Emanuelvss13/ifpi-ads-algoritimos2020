def main():
    n1 = int(input('Digite o 1º numero: '))
    n2 = int(input('Digite o 2º numero: '))
    n3 = int(input('Digite o 3º numero: '))

    verificar = verificar_numeros(n1, n2, n3)

    print(f'Há {verificar} numeros iguais.')

def verificar_numeros(n1, n2, n3):
    if n1 != n2 and n1 != n3 and n2 != n3:
        return 0
    elif n1 != n3 and n1 == n2:
        return 2
    elif n1 != n2 and n1 == n3:
        return 2
    elif n1 != n2 and n2 == n3:
        return 2 
    else:
        return 3
        
main()
