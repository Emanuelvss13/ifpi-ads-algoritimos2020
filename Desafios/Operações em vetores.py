def main():

    menu = '*** Brincando com Listas ***'
    menu += '\n 1 - Inserir Valores'
    menu += '\n 2 - Mostrar Valor posição'
    menu += '\n 3 - Remover do Final'
    menu += '\n 4 - Remover do Início'
    menu += '\n 5 - Remover de Posição Específica'
    menu += '\n 6 - Multiplicar o valor dos dados por um valor especificados'
    menu += '\n 7 - Dividir o valor dos dados por um valor especificados'
    menu += '\n 8 - Mostrar na tela a quantidade de numeros pares, impares'
    menu += '\n 9 - Mostrar na tela a quantidade de numeros positivos, negativos'
    menu += '\n 10 - Mostrar na tela a média dos valores do array'
    menu += '\n 11 - Apagar todos os valores'
    menu += '\n 12 - inserir valor em alguma posição'
    menu += '\n 100 - Mostrar o array na tela'
    menu += "\n 0 - sair"
    menu += '\n\n Opção >>> '

    lista = []

    while True:  # Condição sempre verdadeira, só irá para em caso de break ou error
        opcao = int(input(menu))

        # Verificar operacao a fazer de acordo com a opcao
        if opcao == 1:
            inserir_valores(lista)
        elif opcao == 2:
            mostra_valor(lista)
        elif opcao == 3:
            remover_final(lista)
        elif opcao == 4:
            remover_inicio(lista)
        elif opcao == 5:
            remover_posicao(lista)
        elif opcao == 6:
            multiplicar(lista)
        elif opcao == 7:
            divisao(lista)
        elif opcao == 8:
            pares_impares(lista)
        elif opcao == 9:
            positivos_negativos(lista)
        elif opcao == 10:
            media(lista)
        elif opcao == 11:
            apagar_all(lista)
        elif opcao == 12:
            inserir_valor(lista)
        elif opcao == 100:
            mostrar(lista)
        elif opcao == 0:
            print('Obrigado :)')
            break
        else:
            print('Opção Inválida')


def inserir_valores(lista):
    qtd = int(input('Quantos valores desejar inserir?'))

    for i in range(qtd):
        valor = int(input('Valor: '))
        lista.append(valor)

    print('Valores inseridos com sucesso!')
    input('<enter> to continue...')


def mostra_valor(lista):
    posicao = int(input('Qual posição? '))
    print('Valor buscado:')
    print(lista[posicao])

    input('<enter> to continue...')


def remover_final(lista):
    ult_ele = len(lista)
    lista.pop(ult_ele - 1)

    input('<enter> to continue...')


def remover_inicio(lista):
    lista.pop(0)

    input('<enter> to continue...')


def remover_posicao(lista):
    num = int(input('Digite a posiçao do item que você deseja excluir: '))
    
    if num > len(lista):
        print('Esse item não existe na lista!')
    else:
        print('Item excluido com sucesso :)')
        lista.pop(num)

    input('<enter> to continue...')

def multiplicar(lista):
    num = int(input('Por quanto você deseja multiplicar cada item?: '))
    
    for i in range(len(lista)):
        lista[i] = lista[i] * num

    input('<enter> to continue...')

def divisao(lista):
    num = int(input('Por quanto você deseja dividir cada item?: '))

    for i in range(len(lista)):
        lista[i] = lista[i] / num

    input('<enter> to continue...')


def pares_impares(lista):
    counter_p = 0
    counter_i = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            counter_p += 1
        if lista[i] % 2 != 0:
            counter_i += 1
    
    print(f'Nessa lista tem {counter_p} numeros pares e {counter_i} impares.')

    input('<enter> to continue...')

def positivos_negativos(lista):
    counter_p = 0
    counter_n = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            counter_n += 1
        if lista[i] > 0:
            counter_p += 1
    
    print(f'Nessa lista tem {counter_p} numeros positivos e {counter_n} negativos.')

    input('<enter> to continue...')    


def media(lista):
    counter = 0

    for i in range(len(lista)):
        counter += lista[i]

    print(f'A média dos valores é de: {counter / len(lista)}')


def apagar_all(lista):
    for i in range(len(lista)):
        lista.pop(len(lista) - 1)

def inserir_valor(lista):
    num = int(input('Qual numero você deseja adicionar: '))

    pos = int(input('Em qual posiçâo você deseja adicionar esse número: '))

    if pos > len(lista):
        print('Posição não existente')
    else:
        lista[pos] = num



def mostrar(lista):
    print(f'Até agora o array tem os valores: {lista}')
        


main()