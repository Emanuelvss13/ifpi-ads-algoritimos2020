numerador = 1
denominador = 1

fracao = 0

print(f'{numerador} / {denominador}')

while numerador < 99 and denominador <= 50:
    
    fracao += numerador / denominador

    numerador += 2
    denominador += 1

    print(f'{numerador} / {denominador}')

print(f'O resultado é: {fracao}')

