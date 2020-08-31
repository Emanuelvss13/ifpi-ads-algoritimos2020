n = int(input('Digite um número: '))

fracao = 0

NumDen = 1

for i in range (n,1-1,-1):
    if n % 2 != 0:
        fracao += NumDen/n
        n -= 1
        NumDen += 1
    else:
        fracao -= n/NumDen
        n -= 1
        NumDen += 1

print(fracao)
    