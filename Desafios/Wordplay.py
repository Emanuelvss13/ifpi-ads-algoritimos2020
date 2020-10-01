def main():
    # se nao achar o arquivo
    # https://stackoverflow.com/questions/49143852/trouble-opening-files-in-python-with-vs-code
    # "python.terminal.executeInFileDir": true,

    menu = '##### WordPplay #####\n' \
        + '1 - Palavras com + de 20 letras\n' \
        + '2 - Palavras sem "e"\n' \
        + '3 - testar se uma palavra tem alguma letra proibida\n' \
        + '4 - testar se uma palavra tem alguma letra de uma lista\n' \
        + '5 - testar se uma palavra tem todas as letras de uma lista\n' \
        + '6 - testar se uma palavra esta em ordem alfabetica\n' \
        + '0 - Sair\n' \
        + '\nDigite uma opção: '

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            palavras_com_mais_de_20_letras()
        elif opcao == 2:
            palavras_sem_letra_e()
            # TODO
        elif opcao == 3:
            avoids()
            # TODO
        elif opcao == 4:
            uses_only()
            # TODO
        elif opcao == 5:
            uses_all()
            # TODO
        elif opcao == 6:
            is_abecedarian()
            # TODO
        else:
            print('Opção Inválida!')

        input('continuar <enter> ...')
        opcao = int(input(menu))

    print('Fim wordplay....')


def palavras_com_mais_de_20_letras():
    print('>> Palavras com + de 20 letras \n')
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()
        if len(palavra) > 20:
            print(palavra)

    arquivo.close()


def palavras_sem_letra_e():
    print('>> Palavras sem letra "e" \n')
    arquivo = open('words.txt')
    total = 0
    palavras_sem_e = 0

    for linha in arquivo:
        palavra = linha.strip()
        total += 1
        if has_no_e(palavra):
            palavras_sem_e += 1
            print(palavra)

    perc = (palavras_sem_e / total) * 100
    print(f'Total de Palavras: {total}')
    print(f'Palavras sem "e": {palavras_sem_e}')
    print(f'Percentual {perc} %')
    arquivo.close()


def has_no_e(palavra):
    # return 'e' not in palavra
    for letra in palavra:
        if letra == 'e':
            return False

    return True


def avoids():
    teste = 0
    counter = 0
    arr = []

    palavra = input('Digite uma palavra: ')

    num = int(input('Quantas letra você deseja testar: '))
    
    while counter < num:
        valor = input('Digite uma letra: ')
        arr.append(valor)
        counter += 1

    for i in range(len(arr)):
        for letra in palavra:
            if letra == arr[i]:
                teste += 1

    if teste > 0:
        print(True)
    else:
        print(False)


def uses_only():
    teste = 0
    counter = 0
    arr = []

    palavra = input('Digite uma palavra: ')

    num = int(input('Quantas letra você deseja testar: '))
    
    while counter < num:
        valor = input('Digite uma letra: ')
        arr.append(valor)
        counter += 1

    for i in range(len(arr)):
        for letra in palavra:
            if letra == arr[i]:
                teste += 1

    if teste == 0:
        print(True)
    else:
        print(False)

def uses_all():
    teste = 0
    counter = 0
    arr = []

    palavra = input('Digite uma palavra: ')

    num = int(input('Quantas letra obrigatorias essa palavra deve ter: '))
    
    while counter < num:
        valor = input('Digite uma letra: ')
        arr.append(valor)
        counter += 1

    for i in range(len(arr)):
        for letra in palavra:
            if letra == arr[i]:
                teste += 1

    if teste >= num:
        print(True)
    else:
        print(False)

def is_abecedarian():
    palavra = input('Digite uma palavra: ')
    previous = palavra[0]
    for letra in palavra:
        if letra < previous:
            print(False)
            previous = letra
            break
        else:
            print(True)



main()