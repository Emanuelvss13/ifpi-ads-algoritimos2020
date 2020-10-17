n = int(input('Digite a ordem da matriz: '))
counter = n
dig_s = 0
dig_p = 0
repeteco_p = n
fr_p = 0
repeteco_s = n
fr_s = 0
result = 0 

matriz = []
array = []


# Função para criar a matriz

def adc_linha(matriz, array):
        matriz.append(array)


# Criar a matriz

while counter > 0:
    array = []
    n = repeteco_p
    while n > 0:
        element = int(input('Digite um número: '))
        array.append(element)
        n -= 1

    adc_linha(matriz, array)
    counter -= 1


# Diagonal Principal

while repeteco_p > 0:
    dig_p += matriz[fr_p][repeteco_p - 1] 

    repeteco_p -= 1
    fr_p += 1
    

# Diagonal Secundaria

while repeteco_s > 0:
    dig_s += matriz[fr_s][fr_s] 

    repeteco_s -= 1
    fr_s += 1

# Soma total

s_t = 0

for i in range(len(matriz)):
    for j in range(len(matriz)):
        result += matriz[i][j]
        if i == j:
            s_t += matriz[i][j]


# Soma dos outros números

s_t += result - (dig_p + dig_s)


print(f'A diagonal principal é: {dig_p}, a diagonal secundaria é: {dig_s} e a soma dos outros numeros é: {s_t}')






