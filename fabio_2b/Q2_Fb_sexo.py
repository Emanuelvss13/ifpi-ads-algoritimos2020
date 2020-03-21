def main():
    l = input('Digite uma letra: ')

    sexo(l)

def sexo(l):
    if l == 'm':
        print('Masculino')
    elif l == 'f':
        print('Feminino')
    else:
        print('Sexo inválido')

main()