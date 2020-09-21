msg = input('Digite a mensagem enviada por Sami: ')

counter = 0
msgLength = len(msg)

for i in range(len(msg)):

    if ord(msg[i]) == 79 or ord(msg[i]) == 83:
        counter += 1


msg1 = 'letra'
if counter > 1:
    masg1 = 'letras'


print(f'{msgLength - counter} {msg1} foram alteradas pela radiação!')