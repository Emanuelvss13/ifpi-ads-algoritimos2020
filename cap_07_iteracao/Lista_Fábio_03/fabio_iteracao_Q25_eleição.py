Bolsonaro = 0
Lula = 0
Marina = 0
Branco = 0
Nulo = 0

while True:
    print('==================================')
    print('Digite 1 para votar no Bolsonaro')
    print('Digite 2 para votar no Lula')
    print('Digite 3 para votar na Marina')
    print('Digite 9 para votar em Nulo')
    print('Digite 0 para votar em Branco')
    print('==================================')

    voto = int(input('Digite o número do candidato: '))

    if voto != 1 and voto != 2 and voto != 3 and voto !=9  and voto != 0:
        
        if Bolsonaro > Lula and Bolsonaro > Marina:
            resultado = 'Vitoria do Bolsonaro'
        elif Lula > Bolsonaro and Lula > Marina:
            resultado = 'Vitoria do Lula'
        elif Marina > Bolsonaro and Marina > Lula:
            resultado = 'Vitoria da Marina'
        else:
            resultado = 'Eleição sem Vencedor'
        

        print(f'O Bolsonaro teve:{Bolsonaro} voto(s)')
        print(f'O Lula teve: {Lula} voto(s)')
        print(f'A Marina teve: {Marina} voto(s)')
        print(f'Foram {Nulo} voto(s) Nulos')
        print(f'Foram {Branco} voto(s) em Branco')
        print(f'O resulatodo da eleição é: {resultado}')
        break
    else:
        if voto == 1:
            Bolsonaro += 1
        elif voto == 2:
            Lula += 1
        elif voto == 3:
            Marina += 1
        elif voto == 9:
            Nulo += 1
        elif voto == 0:
            Branco += 1
        