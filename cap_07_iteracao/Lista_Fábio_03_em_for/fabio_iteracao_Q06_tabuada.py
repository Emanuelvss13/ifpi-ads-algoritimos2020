def main():
    numero = int(input('Digite um número: '))
    operacao = int(input('1-multiplicação | 2-Divisão | 3-subtração | 4-Adição: '))

    valor = 1
    contador = 0

    if operacao == 1:
        print(f'Tabuada de Multiplicaçao de {numero}\n')
        for i in range(valor, 10+1):
            print(f'{numero} x {valor} = {numero * valor}')
            valor += 1

    elif operacao == 2:
        print(f'Tabuada de divisão de {numero}\n')
        for i in range(valor, 10+1):
            resultado = numero * valor
            print(f'{resultado} ÷ {numero} = {valor}')
            valor += 1

    elif operacao == 3:
        valor = numero
        print(f'Tabuada de Subtração de {numero}\n')
        for i in range(contador, 10+1):
            print(f'{valor} - {numero} = {valor - numero}')
            valor += 1
            contador += 1

    elif operacao == 4:
        valor = 0
        print(f'Tabuada de Adição de {numero}\n')
        for i in range(valor, 10+1):
            print(f'{numero} + {valor} = {numero + valor}')
            valor += 1 



main()