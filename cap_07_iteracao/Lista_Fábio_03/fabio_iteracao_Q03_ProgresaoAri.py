def main():
    a = int(input('Digite o A0: '))
    limite = int(input('Digite o Limite: '))
    razao = int(input('Digite a Razão: '))

    termo = 1

    if a < 0 and limite < 0:
        while a > limite:
            print(f'termo {termo}º = {a}')
            a -= razao
            termo += 1
    else:
        while a < limite:
            print(f'termo {termo}º = {a}')
            a += razao
            termo += 1
            

    print(f'O limite é: {limite}')
    

main()