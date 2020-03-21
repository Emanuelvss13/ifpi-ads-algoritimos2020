def main():
    altura = float(input('Digite a sua altura: '))
    peso = float(input('Digite seu peso: '))

    imc(altura, peso)


def imc(altura, peso):
    imc = peso / altura ** 2
    if imc < 25:
        print('seu peso está normal.')
    elif imc >= 25 and imc <= 30:
        print('Você está obeso')
    else:
        print('Você está com obesidade morbida.')


main()