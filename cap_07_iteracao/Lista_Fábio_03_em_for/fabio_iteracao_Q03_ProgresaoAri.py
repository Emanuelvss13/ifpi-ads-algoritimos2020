def main():
    a = int(input('Digite o A0: '))
    limite = int(input('Digite o Limite: '))
    razao = int(input('Digite a Razão: '))


    for i in range(a, limite+1, razao):
        print(i)


main()