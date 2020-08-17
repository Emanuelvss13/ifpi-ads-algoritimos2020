def main():
    limiteInferior = int(input('Digite o Limite Inferior: '))
    limiteSuperior = int(input('Digite o Limite Superior: '))

    if limiteInferior <= 0:
        print('O limite inferior tem que ser acima de zero(0).')
    else:    
        while limiteInferior <= limiteSuperior:

            if limiteInferior % limiteInferior == 0 and limiteInferior % 2 != 0 and limiteInferior % 3 != 0 and limiteInferior % 5 != 0 and limiteInferior % 7 != 0:
                print(limiteInferior)
                limiteInferior = limiteInferior + 1   
                continue
            elif limiteInferior == 2 or limiteInferior == 3 or limiteInferior == 5 or limiteInferior == 7:
                print(limiteInferior)
                limiteInferior += 1  
            else:
                limiteInferior += 1    



main()