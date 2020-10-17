array = []

while True:
    element = input('Digite um número ou exit para sair: ')

    if element == 'exit':
        iguais = 0
        for i in range(len(array)):
            for j in range(len(array)):
                if array[i] == array[j]:
                    if j == i:
                        j += 1
                        continue
                    else:
                        iguais += 1
                        break
        break

    array.append(int(element))

print(f'O array tem {len(array)} elemento e {iguais} são iguais')
print(array)



    