def main():
    limiteInferior = int(input('Digite o Limite Inferior: '))
    limiteSuperior = int(input('Digite o Limite Superior: '))
    


    for i in range( limiteInferior, limiteSuperior+1):

        if limiteInferior % 2 != 0:
            print(limiteInferior)
            limiteInferior = limiteInferior + 1   
            continue
        else:
            limiteInferior += 1    



main()