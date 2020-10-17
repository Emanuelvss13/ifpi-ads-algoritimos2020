n = int(input('Digite a ordem da matriz: '))
matriz = []
array = []
counter = n
repeteco = n

def adc_linha(matriz, array):
        matriz.append(array)


# Criar a matriz

while counter > 0:
    array =[]
    n = repeteco
    while n > 0:
        element = int(input('Digite um número: '))
        array.append(element)
        n -= 1

    adc_linha(matriz, array)
    counter -= 1


temp = 0
real_ma = 0
real_me = 1000000000000000000000000000000000000000000000000000000000000000000000000000000



for i in range(len(matriz)):
    for j in range(len(matriz)):
        temp += matriz[i][j]
    
    if temp > real_ma:
        real_ma = temp

    if temp < real_me:
        real_me = temp

    temp = 0





print(f'a maior em relação a soma é: {real_ma}, e a menor é: {real_me}')

print(f'Essa é sua matriz: {matriz}')




