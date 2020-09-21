palavra = input('Digite uma palavra:')

arvalap = ''
counter = 0
counter1 = 1

funny_or_not = 0
limite = len(palavra)

for i in range(limite-1,-1, -1):
    arvalap += palavra[i]


while counter1 < limite:
    if ord(palavra[counter]) - ord(palavra[counter1]) == ord(arvalap[counter1]) - ord(arvalap[counter]):
        funny_or_not += 1
    if ord(palavra[counter]) - ord(palavra[counter1]) != ord(arvalap[counter1]) - ord(arvalap[counter]):
        funny_or_not -= 1000
    
    counter1 += 1
    counter += 1


if funny_or_not < 0:
    print('Not Funny :(')
elif funny_or_not > 0:
    print('Funny :)')
    
