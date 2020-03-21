def main():
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    n3 = int(input('Digite o 3º número: '))
    n4 = int(input('Digite o 4º número: '))
    n5 = int(input('Digite o 5º número: '))

    media(n1, n2, n3, n4, n5)


def media(n1, n2, n3, n4, n5):      
    m = (n1 + n2 + n3 + n4 + n5) // 5
    if n1 > m:
        print(n1, end= ',')
    if n2 > m:
        print(n2, end= ',')
    if n3 > m:
        print(n3, end= ',')
    if n4 > m:
        print(n4, end= ',')
    if n5 > m:
        print (n5, end= ',')

main()