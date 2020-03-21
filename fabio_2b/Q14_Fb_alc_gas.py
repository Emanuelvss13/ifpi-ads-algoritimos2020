def main():
    litros = float(input('Digite quantos litros foram vendidos: '))
    tipo = input('Qual tipo foi comprado: ')

    combustivel(litros, tipo)

def combustivel(litros, tipo):
    if tipo == 'A' or tipo == 'a' and litros <= 20:
        valor = litros * 1.90
        desconto = valor * (3/100)
        valor_c_desconto = valor - desconto
        print(f'O valor a ser pago é: {valor_c_desconto}')
    elif tipo == 'A' or tipo == 'a' and litros > 20:
        valor = litros * 1.90
        desconto = valor * (5/100)
        valor_c_desconto = valor - desconto
        print(f'O valor a ser pago é: {valor_c_desconto}')
    elif tipo == 'G' or tipo == 'g' and litros <= 20:
        valor = litros * 2.50
        desconto = valor * (4/100)
        valor_c_desconto = valor - desconto
        print(f'O valor a ser pago é: {valor_c_desconto}')
    elif tipo == 'G' or tipo == 'g' and litros > 20:
        valor = litros * 2.50
        desconto = valor * (6/100)
        valor_c_desconto = valor - desconto
        print(f'O valor a ser pago é: {valor_c_desconto}')

main()


