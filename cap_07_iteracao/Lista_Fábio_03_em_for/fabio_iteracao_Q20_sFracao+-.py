n = int(input('Digite um número: '))

fracao = 0

contador = 1

for i in range (1,n+1):
    if contador % 2 != 0:
        fracao += 1 / contador
        contador += 1
    else:
        fracao -= 1 / contador
        contador += 1

print(fracao)
    