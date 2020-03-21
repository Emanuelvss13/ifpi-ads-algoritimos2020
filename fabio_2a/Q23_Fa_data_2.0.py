def main():
    d = int(input('Digite 1º dia: '))
    m = int(input('Digite 1º mês: '))
    a = int(input('Digite 1º ano: '))

    d2 = int(input('Digite 2º dia: '))
    m2 = int(input('Digite 2º mês: '))
    a2 = int(input('Digite 2º ano: '))

    recente(d, m, a, d2, m2, a2)

def recente(d, m, a, d2, m2, a2):
    if a < a2:
        print('A data mais recente é a 2º.')
    elif a > a2:
        print('A data mais recente é a 1º.')
    elif d2 > d and m == m2 and a == a2:
        print('A data mais recente é a 2º.')
    elif d > d2 and m == m2 and a == a2:
        print('A data mais recente é a 1º.')
        


main()