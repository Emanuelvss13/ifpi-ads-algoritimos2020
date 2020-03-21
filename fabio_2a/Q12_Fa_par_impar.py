def main():
    n = int(input('Digite um número: '))

    resultado = par_impar(n)

    print(resultado)


def par_impar(n):
    if n % 10 == 0 or n % 10 == 2 or n % 10 == 4 or n % 10 == 6 or n % 10 == 8:
        return 'Esse número é par.'
    else:
        return 'Esse número é impar.'

main()
