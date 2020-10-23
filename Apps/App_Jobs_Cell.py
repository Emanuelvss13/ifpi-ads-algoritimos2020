import os
import json
import re


def main():

    celulares = carregar_cel('celulares.bd')

    while True:
        tela_inicial()
        option = int(input('Digite uma opção: '))

        if option == 1:
            celular = adc_cel()
            celulares.append(celular)
        elif option == 2:
            list_cel(celulares)
            input("Pressione qualquer tecla para continuar...")
        elif option == 3:
            pesquisa(celulares)
            input("Pressione qualquer tecla para continuar...")
        elif option == 0:
            salvar_cel('celulares.bd', celulares)
            break
        else:
            print('Você digitou uma opção inválida')



##### FUNÇÕES #####


def tela_inicial():
    print(25*'=')
    print(' 1 << Adicionar celular')
    print(' 2 << Listar todos os celulares')
    print(' 3 << Pesquisar')
    print(' 0 << Sair do app')
    print(25*'=')


def adc_cel():
    marca = input('Digite a marca do celular: ')
    modelo = input('Digite o modelo do celular: ')
    preco = int(input('Digite o preço do celular: '))
    func = input('Digite as funcionabilidades do celular: ')

    celular = {
        'marca': marca,
        'modelo': modelo,
        'preço': preco,
        'funcionabilidades': func
    }

    return celular

    

def list_cel(celulares):
    if len(celulares) <= 1:
        result = 'celular'
    else:
        result = 'celulares'
    
    print(f'Encontramos {len(celulares)} {result}')

    print(25*'=')
    def render(celulares):
        for linha in celular:
            print(f'{linha}: {celular[linha]}')

    for celular in celulares:
        render(celular)
        print(25*'=')
    

def carregar_cel(file):
    celulares = []

    if os.path.exists(file):
        arquivo = open(file)
        dados = arquivo.readline()
        celulares = json.loads(dados)

    return celulares


def salvar_cel(file, celulares):
    dados = json.dumps(celulares)
    arquivo = open(file, 'w')
    arquivo.write(dados)


def tela_inicial_2():
    print(25*'=')
    print(' 1 << Mostar detalhes')
    print(' 2 << Remover celular')
    print(' 3 << Editar')
    print(' 4 << Duplicar celular')
    print(25*'=')

def list_cel_2(celulares):
    print(25*'=')
    def render(celulares):
        for linha in celular:
            if linha == 'preço':
                break
            print(f'{linha}: {celular[linha]}')

    for celular in celulares:
        render(celular)
        print(25*'=')


def mostrar_detalhes(selecionado):
    print(25*'=')
    for linha in selecionado:
        print(f'{linha}: {selecionado[linha]}')
    print(25*'=')


def remover(selecionado, celulares):
    print(25*'=')
    celulares.remove(selecionado)
    print('Celular removido com sucesso')
    print(25*'=')


def editar(selecionado, celulares):
    
    marca = input('Digite a marca do celular: ')
    modelo = input('Digite o modelo do celular: ')
    preco = int(input('Digite o preço do celular: '))
    func = input('Digite as funcionabilidades do celular: ')

    selecionado['marca'] = marca
    selecionado['modelo'] = modelo
    selecionado['preço'] = preco
    selecionado['funcionabilidades'] = func

def duplicar(selecionado):
    
    celular = {
        'marca': selecionado['marca'],
        'modelo': selecionado['modelo'],
        'preço': selecionado['preço'],
        'funcionabilidades': selecionado['funcionabilidades']
    }

    print('Celular Duplicado com sucesso')
    input("Pressione qualquer tecla para continuar...")
    return celular


def pesquisa(celulares):
    achados = []
    qtd = 0
    tipo = input('Você deseja pesquisar por modelos ou por marcas? ')


    if tipo == 'modelo':
        const = 'modelo'
        palavra = input('Digite o modelo: ')
    elif tipo == 'marca':
        const = 'marca'
        palavra = input('Digite a marca: ')
    else:
        print('Opa parece que você digitu algo errado :(')
        input("Pressione qualquer tecla para continuar...")
        main()

    for i in range(len(celulares)):
        asd = celulares[i][const]
        if re.search(palavra, asd, re.IGNORECASE) == None:
            continue
        else:
            achados.append(celulares[i])
            qtd += 1

    list_cel_2(achados)
    
    print(f'Encontramos {qtd} resultados referentes a pesquisa')
    input("Pressione qualquer tecla para continuar...")

    if qtd == 0:
        main()


    selecionar = int(input("Selecione um celular: "))

    selecionado = celulares[selecionar - 1]

    tela_inicial_2()

    option = int(input('Digite uma opção: '))

    if option == 1:
        mostrar_detalhes(selecionado)
    elif option == 2:
        remover(selecionado, celulares)
    elif option == 3:
        editar(selecionado, celulares)
    elif option == 4:
        celular = duplicar(selecionado)
        celulares.append(celular)
    else:
        print('Opa parece que você digitu algo errado :(')
        input("Pressione qualquer tecla para continuar...")
        main()


main()





####################
#Emanuel-23/10/2020#
####################