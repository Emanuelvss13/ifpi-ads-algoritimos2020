n = int(input('Digite um número: '))

fracao = 0

contador = 1

while contador <= n:
    if contador % 2 != 0:
        fracao += 1 / contador
        contador += 1
    else:
        fracao -= 1 / contador
        contador += 1

print(fracao)
    