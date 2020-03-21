def main():
    d = int(input('Digite o dia em que voçe nasceu: '))
    m = int(input('Digite o mês em que voçe nasceu: '))
    a = int(input('Digite o ano em que voçe nasceu: '))

    d2 = int(input('Que dia é hoje: '))
    m2 = int(input('Qual é o mês atual: '))
    a2 = int(input('Em que ano estamos: '))

    idade(d, m, a, d2, m2, a2)

def idade(d, m, a, d2, m2, a2):
    if d2 >= d and m2 >= m:
        meses = m2 - m
        dias = d2 - d
        ano = a2 - a
        print(f'A sua idade é igual a: {ano} anos, {meses} meses e {dias} dias.')
    elif m2 < m and d2 >= d:
        meses = 12 + (m2 - m)
        dias = d2 - d
        ano = (a2 - a) - 1
        print(f'A sua idade é igual a: {ano} anos, {meses} meses e {dias} dias.')
    elif d2 > d and m2 < m:
        meses = 12 + (m2 - m) - 1
        dias = 30 + (d2 - d) - 1
        ano = (a2 - a) - 1
        print(f'A sua idade é igual a: {ano} anos, {meses} meses e {dias} dias.')

main()