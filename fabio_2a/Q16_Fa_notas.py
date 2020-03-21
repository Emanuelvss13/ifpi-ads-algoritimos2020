def main():
    n1 = float(input('Digite a sua 1º nota: '))
    n2 = float(input('Digite a sua 2º nota: '))
    
    resultado = nota(n1, n2)
    
    print(resultado)

def nota(n1, n2):
    media = (n1 + n2) / 2
    if media >= 7:
        return 'Aprovado !'
    else:
        n3 = float(input('Digite a nota da recuperação: '))
        media_2 = (n1 + n2 + n3) / 3
        if media_2 >= 5:
            return 'Aprovado !'
        elif media_2 < 5:
            return 'Reprovado !'

main()