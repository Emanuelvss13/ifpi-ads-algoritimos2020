array = []

counter = int(input('Digite quantos números você quer colocar no array: '))


while counter > 0:
    element = int(input('Digite um número: '))

    array.append(element)

    counter -= 1



for i in range(len(array)):
    for j in range(len(array)):
        if array[j] > array[i]:
            maior = array[j]
            indice = j

def menor(array):
    mini = min(array)
    for i in range(len(array)):
        if array[i] == mini:
            indice = i
    return indice

            
print(f'O maior número é: {maior} de indice: {indice}, e o menor é: {min(array)} com indice: {menor(array)}')
