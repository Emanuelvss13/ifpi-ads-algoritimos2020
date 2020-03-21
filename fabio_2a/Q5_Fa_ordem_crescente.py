def main():
    
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    n3 = int(input('Digite o 3º número: '))

    resultado = crescente(n1, n2, n3)

    print(resultado)


def crescente(n1, n2, n3):
    if n1 < n2 < n3:
        return f'A ordem crescente é {n1}, {n2}, {n3}.'
    
    elif n1 < n3 < n2:
        return f'A ordem crescente é {n1}, {n3}, {n2}.'
    
    elif n2 < n1 < n3:
        return f'A ordem crescente é {n2}, {n1}, {n3}.' 
    
    elif n2 < n3 < n1:
        return f'A ordem crescente é {n2}, {n3}, {n1}.'
    
    elif n3 < n1 < n2:
        return f'A ordem crescente é {n3}, {n1}, {n2}.'
    
    else:
        return f'A ordem crescente é {n3}, {n2}, {n1}.'


main()

