def main():
    d = int(input('Digite um dia: '))
    m = int(input('Digite um mês: '))
    a = int(input('Digite um ano: '))

    resultado = data(d, m, a)

    print(resultado)


def data(d, m, a):
    
    if m == 1 and 3 and 5 and 7 and 8 and 10 and 12 or d <= 31:
        return 'essa data é válida.'
    
    elif m == 4 and 6 and 9 and 11 or d <= 30:
        return 'essa data é válida.'

    elif m == 2 or d <= 28:
        return 'essa data é válida.'
    
    else:
        return 'essa data é inválida.'

main()

#def bissexto:
#elif a%4 == 0:
# if m == 2 and d > 29:    
#if a%100 != 0:
#if m == 2 and d > 29:
#if a%400 == 0:
#if m == 2 and d > 29:                
# return 'essa data é inválida.'