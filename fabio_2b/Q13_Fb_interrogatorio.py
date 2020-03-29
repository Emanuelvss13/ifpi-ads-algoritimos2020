def main():
    p1 = input('Telefonou para a vitima ?\n responda sim ou nao: ')
    p2 = input('Esteve no local do crime ?\n responda sim ou nao: ')
    p3 = input('Mora perto da vitima ?\n responda sim ou nao: ')
    p4 = input('Devia para vitima ?\n responda sim ou nao: ')
    p5 = input('Já trabalhou com a vitima ?\n responda sim ou nao: ')
    
    s = 0
    
    
    
    interrogatorio(p1, p2, p3, p4, p5, s)


def interrogatorio(p1, p2, p3, p4, p5, s):
    if p1 == 'sim':
        s = s + 1
    if p2 == 'sim':
        s = s + 1
    if p3 == 'sim':
        s = s + 1
    if p4 == 'sim':
        s = s+ 1
    if p5 == 'sim':
        s = s + 1
    contador(s)
    return s


def contador(s):
    if s == 2:
        print('SUSPEITO!')
    if s == 4:
        print('CÚMPLICE!')
    if s == 5:
        print('ASSASINO!')
    if s == 0: 
        print('INOCENTE!')
    if s == 1:
        print('INOCENTE!')
    if s == 3:
        print('INOCENTE!')


main()