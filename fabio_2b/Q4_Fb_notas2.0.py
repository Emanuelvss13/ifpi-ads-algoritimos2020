def main():
    n1 = int(input('Digite sua 1º nota: '))
    n2 = int(input('Digite sua 2º nota: '))

    notas(n1, n2)


def notas(n1, n2):
    media = (n1 + n2) / 2
    if media >= 7:
        print('Aprovado')
    if media == 10:
        print('Aprovado com distinção')
    else:
        print('Reprovado')

main()
    
