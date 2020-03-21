def main():
    n = float(input('Digite um número: '))
    
    de_num(n)



def de_num(n):
    if n % 1 == 0:
        print('numerico')
    else:
        print('Decimal')

main()
