def main():
    d1 = int(input('Digite o dia em que voçe nasceu: '))
    m1 = int(input('Digite o mês em que voçe nasceu: '))
    a1 = int(input('Digite o ano em que voçe nasceu: '))

    d2 = int(input('Que dia é hoje: '))
    m2 = int(input('Qual é o mês atual: '))
    a2 = int(input('Em que ano estamos: '))

    resultado = aniversario(d1, m1, a1, d2, m2, a2)

    print(resultado)



def aniversario(d1, m1, a1, d2, m2, a2):     
    if d2 < d1 and m2 < m1:
        anos = a2 - a1
        idade =  anos - 1
    
        return f'Voçe tem exatamente {idade} anos.'

    elif d2 >= d1 and m2 >= m1: 
        ano = a2 - a1
        
        return f'Voçe tem exatamente {ano} anos.'

main()  