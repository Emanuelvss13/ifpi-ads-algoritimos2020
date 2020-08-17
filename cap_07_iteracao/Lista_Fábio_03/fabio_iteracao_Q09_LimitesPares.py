def main():
    limiteInferior = int(input('Digite o Limite Inferior: '))
    limiteSuperior = int(input('Digite o Limite Superior: '))
    


    while limiteInferior <= limiteSuperior:

        if limiteInferior % 2 == 0:
            print(limiteInferior)
            limiteInferior = limiteInferior + 1   
            continue
        else:
            limiteInferior += 1    



main()