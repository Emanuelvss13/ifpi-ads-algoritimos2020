counter = 0
array = []
decimal = []
hexadecimal = []


while counter < 8:
    element = int(input('Digite o número binário um número por vez: '))

    if element != 0 and element != 1:
        print('error 400 (Digite 1 ou 0)')
        break

    array.append(element)
    counter += 1


def to_decimal(array):
    for i in range(len(array)):
            decimal.append(array[i])

    decimal.reverse()
    dec = 0
    number = len(decimal) - 1

    while number >= 0:
            result = decimal[number] * (2 ** number)
            dec += result
            number -= 1
    return dec

def verificar(p_1):
    if p_1[0] == 1 and p_1[1] == 0 and p_1[2] == 0 and p_1[3] == 0:
        return 8 
    elif p_1[0] == 1 and p_1[1] == 0 and p_1[2] == 0 and p_1[3] == 1:
        return 9
    elif p_1[0] == 1 and p_1[1] == 0 and p_1[2] == 1 and p_1[3] == 0:
        return 'A'
    elif p_1[0] == 1 and p_1[1] == 0 and p_1[2] == 1 and p_1[3] == 1:
        return 'B'
    elif p_1[0] == 1 and p_1[1] == 1 and p_1[2] == 0 and p_1[3] == 0:
        return 'C'
    elif p_1[0] == 1 and p_1[1] == 1 and p_1[2] == 0 and p_1[3] == 1:
        return 'D'
    elif p_1[0] == 1 and p_1[1] == 1 and p_1[2] == 1 and p_1[3] == 0:
        return 'E'
    elif p_1[0] == 1 and p_1[1] == 1 and p_1[2] == 1 and p_1[3] == 1:
        return 'F'

p_1 = []
p_2 = []

for i in range(len(array)):
    if i <= 3:
        p_1.append(array[i])
    else:
        p_2.append(array[i])


print(f'Esse número em decimal é:{to_decimal(array)} e em Hexadecimal é: {verificar(p_1) + verificar(p_2)}')








