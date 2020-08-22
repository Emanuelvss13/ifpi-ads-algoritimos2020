n = int(input('Digite um número: '))

fracao = 0

NumDen = 1

while n >= 1:
    if n % 2 != 0:
        fracao += NumDen/n
        n -= 1
        NumDen += 1
    else:
        fracao -= n/NumDen
        n -= 1
        NumDen += 1

print(fracao)
    