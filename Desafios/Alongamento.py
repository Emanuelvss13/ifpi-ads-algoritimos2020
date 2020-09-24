qnt = int(input('Quantos números você pretende digitar?: '))

counter = 0

counter_par = 0
counter_impar = 0
counter_negativo = 0
counter_positivo = 0

counter_par2 = 0
counter_impar2 = 0
counter_negativo2 = 0
counter_positivo2 = 0

arr = [-1]*qnt
arr2 = [-1]*qnt

media = 0
print('-----------------------------------------------')
while counter < qnt:
    numero = int(input('Digite um número: '))
    arr[counter] = numero
    if numero > 0:
        counter_positivo += 1
    if numero < 0:
        counter_negativo += 1
    if numero % 2 == 0:
        counter_par += 1
    if numero % 2 != 0:
        counter_impar += 1

    if counter % 2 == 0:
        arr2[counter] = arr[counter] * 2
    else:
        arr2[counter] = arr[counter] / 2

    if arr2[counter] > 0:
        counter_positivo2 += 1
    if arr2[counter] < 0:
        counter_negativo2 += 1
    if arr2[counter] % 2 == 0:
        counter_par2 += 1
    if arr2[counter] % 2 != 0:
        counter_impar2 += 1

    media += arr2[counter]

    counter += 1

print('-----------------------------------------------')


print(f'Você digitou {counter_positivo} números positivos.')
print(f'Você digitou {counter_negativo} números negativo.')
print(f'Você digitou {counter_par} números par.')
print(f'Você digitou {counter_impar} números impar.')
print('-----------------------------------------------')
print(f'O array transformado tem {counter_positivo2} números positivos.')
print(f'O array transformado tem {counter_negativo2} números negativo.')
print(f'O array transformado tem {counter_par2} números par.')
print(f'O array transformado tem {counter_impar2} números impar.')
print('-----------------------------------------------')
print(f'O array que você digitou é: {arr}')
print('-----------------------------------------------')
print(f'Esse array transformado ficou assim: {arr2}')
print('-----------------------------------------------')
print(f'A média do array transformado é: {media / qnt}')