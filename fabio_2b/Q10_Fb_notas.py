def main():
    n1 = float(input('Digite sua 1º nota: '))
    n2 = float(input('Digite sua 2º nota: '))

    notas(n1, n2)

def notas(n1, n2):
    media = (n1 + n2) / 2
    if media > 0 and media < 4:
        print(f'Suas notas foram {n1} e {n2}, sua média foi {media}, você tirou um E, consequentemente você esta Reprovado.')
    
    elif media >= 4 and media < 6:
        print(f'Suas notas foram {n1} e {n2}, sua média foi {media}, você tirou um D, consequentemente você esta Reprovado.')
    
    elif media >= 6 and media < 7.5:
        print(f'Suas notas foram {n1} e {n2}, sua média foi {media}, você tirou um C, consequentemente você esta Aprovado.')

    elif media >= 7.5 and media < 9:
        print(f'Suas notas foram {n1} e {n2}, sua média foi {media}, você tirou um B, consequentemente você esta Aprovado.')

    elif media >= 9 and media <= 10:
        print(f'Suas notas foram {n1} e {n2}, sua média foi {media}, você tirou um A, consequentemente você esta Aprovado.')


main()