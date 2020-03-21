def main():
    p1 = input('Telefonou para a vitima ?\n responda sim ou nao: ')
    p2 = input('Esteve no local do crime ?\n responda sim ou nao: ')
    p3 = input('Mora perto da vitima ?\n responda sim ou nao: ')
    p4 = input('Devia para vitima ?\n responda sim ou nao: ')
    p5 = input('Já trabalhou com a vitima ?\n responda sim ou nao: ')

    interrogatorio(p1, p2, p3, p4, p5)

def interrogatorio(p1, p2, p3, p4, p5):
    if p2 == 'sim' and p1 == 'nao' and p3 == 'nao' and p4 == 'nao' and p5 == 'nao':
        print('Você esta sendo considerado(a) Suspeito! ')
    elif p3 == 'sim' and p4 == 'sim'and p1 == 'nao' and p2 == 'nao' and p5 == 'nao':
        print('Você esta sendo considerado(a) Cúmplice!')
    elif p5 == 'sim'and p4 == 'nao' and p3 == 'nao' and p2 == 'nao' and p1 == 'nao':
        print('VOCÊ É O ASSASINO!')
    else:
        print('Você é inocente.')

main()