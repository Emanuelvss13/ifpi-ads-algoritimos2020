def main():
    
    n = int(input('Digite um número de 1 a 100: '))

    resultado = primo(n)

    print(resultado)

def primo(n):
    if n > 100:
        return 'Digite apenas números entre 0 a 100 !'
    elif n == 2 or n == 3 or n == 5 :
        return 'Esse numero é primo.'
    elif n % 2 == 0 or n % 3 == 0 or n % 4 == 0 or n % 5 == 0:
        return 'Esse número não é primo.'
    elif n % 1 == 0 and n % n == 0:
        return 'Esse numero é primo.'

main()
    