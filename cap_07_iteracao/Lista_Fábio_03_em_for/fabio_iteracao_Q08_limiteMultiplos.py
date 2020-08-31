def main():
    variavel_n = int(input('Digite um número: '))
    limiteSuperior = int(input('Digite o Limite Superior: '))
    limiteInferior = int(input('Digite o Limite Inferior: '))


    for i in range( limiteInferior, limiteSuperior+1):

        if limiteInferior % variavel_n == 0:
            print(limiteInferior)
            limiteInferior = limiteInferior + 1   
            continue
        else:
            limiteInferior += 1    



main()