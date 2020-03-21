def main():
    p1 = float(input('Digite o preço do 1º produto: '))
    p2 = float(input('Digite o preço do 2º produto: '))
    p3 = float(input('Digite o preço do 3º produto: '))

    produto(p1, p2, p3)

def produto(p1, p2, p3):
    if p1 < p2 and p1 < p3:
        print('O primeiro produto deve ser comprado.')
    elif p2 < p1 and p2 < p3:
        print('O segundo produto deve ser comprado.')
    elif p3 < p1 and p3 < p2:
        print('O terceiro produto deve ser comprado.')
    else:
        print('Ai tu escolhe :)')

main()