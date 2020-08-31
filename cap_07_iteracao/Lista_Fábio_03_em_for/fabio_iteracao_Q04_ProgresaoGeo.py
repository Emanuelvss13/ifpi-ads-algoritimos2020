def main():
    a = int(input('Digite o A0: '))
    limite = int(input('Digite o Limite: '))
    razao = int(input('Digite a Razão: '))

    termo = 1

    if a < 0 and limite < 0:
        for i in range(a, limite):
            print(f'termo {termo}º = {a}')
            a *= razao
            termo += 1
            a += 1
            if a < limite:
                break
    else:
        for i in range (a, limite):
            print(f'termo {termo}º = {a}')
            a *= razao
            termo += 1
            if a > limite:
                break
            
            
    print(f'O limite é: {limite}')
    

main()