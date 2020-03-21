def main():
    t = input('Diga qual é o seu turno; M, V ou N ?: ')

    turno(t)

def turno(t):
    if t == 'M' or t == 'm':
        print('Bom Dia!')
    elif t == 'V' or t == 'v':
        print('Boa Tarde!')
    elif t == 'N' or t == 'n':
        print('Boa Noite!')
    else:
        print('Valor Inválido')

main()