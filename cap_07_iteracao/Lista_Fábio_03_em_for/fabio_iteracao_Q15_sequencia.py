def main():
    variavel_n = int(input('Digite um número: '))
    comeco_sequencia = int(input('Digite quantos números devem aparecer após o primeiro: '))


    sequencia = 2
    contador = 0
    print(variavel_n)
    for i in range(contador, comeco_sequencia):
        variavel_n = sequencia + variavel_n
        sequencia += 1
        contador += 1
        print(variavel_n)

main()