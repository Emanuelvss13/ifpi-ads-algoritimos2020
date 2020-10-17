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


simetrica = 0
n_simetrica = 0
result = ''

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] == matriz[j][i]:
            simetrica += 1
        else:
            n_simetrica += 1

# Simetrica ou não

if simetrica > n_simetrica:
    result = 'Simetrica'
else:
    result = 'Não Simetrica'



print(f"Sua matriz é: {matriz} e ela é {result}")