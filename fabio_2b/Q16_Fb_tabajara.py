def main():
    quantidade = float(input('Digite quantos Kg foram comprados: '))
    tipo_da_carne = input('Digite qual tipo de carne o cliente comprou: file, alcatra ou picanha :')
    cartao = input('Digite sim se a compra foi no cartão, caso nao seja, digite nao: ')
    
    carne(quantidade, tipo_da_carne, cartao)

def carne(quantidade, tipo_da_carne, cartao):
    if quantidade <= 5 and tipo_da_carne == 'file' and cartao == 'nao':
        preço_total = quantidade * 4.90
        desconto = 0
        print(f'=====CUPOM FISCAL=====\n Tipo da carne:     {tipo_da_carne}\n Preço total:     {preço_total}\nTipo de pagamento:     Dinheiro\n Valor do desconto:     {desconto}\n Preço a pagar:     {preço_total}')

    elif quantidade <= 5 and tipo_da_carne == 'alcatra' and cartao == 'nao':
        preço_total = quantidade * 5.90
        desconto = 0
        print(f'=====CUPOM FISCAL=====\n Tipo da carne:     {tipo_da_carne}\n Preço total:     {preço_total}\nTipo de pagamento:     Dinheiro\n Valor do desconto:     {desconto}\n Preço a pagar:     {preço_total}')

    elif quantidade <= 5 and tipo_da_carne == 'picanha' and cartao == 'nao':
        preço_total = quantidade * 6.90
        desconto = 0
        print(f'=====CUPOM FISCAL=====\n Tipo da carne:     {tipo_da_carne}\n Preço total:     {preço_total}\nTipo de pagamento:     Dinheiro\n Valor do desconto:     {desconto}\n Preço a pagar:     {preço_total}')

    elif quantidade <= 5 and tipo_da_carne == 'file' and cartao == 'sim':
        preço_total = quantidade * 4.90
        desconto = preço_total * (5/100)
        valor_total = preço_total - desconto
        print(f'=====CUPOM FISCAL=====\n Tipo da carne:     {tipo_da_carne}\n Preço total:     {preço_total}\nTipo de pagamento:     Cartão\n Valor do desconto:     {desconto}\n Preço a pagar:     {valor_total}')

    elif quantidade <= 5 and tipo_da_carne == 'alcatra' and cartao == 'sim':
        preço_total = quantidade * 5.90
        desconto = preço_total * (5/100)
        valor_total = preço_total - desconto
        print(f'=====CUPOM FISCAL=====\n Tipo da carne:     {tipo_da_carne}\n Preço total:     {preço_total}\nTipo de pagamento:     Cartão\n Valor do desconto:     {desconto}\n Preço a pagar:     {valor_total}')

    elif quantidade <= 5 and tipo_da_carne == 'picanha' and cartao == 'sim':
        preço_total = quantidade * 6.90
        desconto = preço_total * (5/100)
        valor_total = preço_total - desconto
        print(f'=====CUPOM FISCAL=====\n Tipo da carne:     {tipo_da_carne}\n Preço total:     {preço_total}\nTipo de pagamento:     Cartão\n Valor do desconto:     {desconto}\n Preço a pagar:     {valor_total}')

    elif quantidade > 5 and tipo_da_carne == 'file' and cartao == 'nao':
        preço_total = quantidade * 4.90
        desconto = 0
        print(f'=====CUPOM FISCAL=====\n Tipo da carne:     {tipo_da_carne}\n Preço total:     {preço_total}\nTipo de pagamento:     Dinheiro\n Valor do desconto:     {desconto}\n Preço a pagar:     {preço_total}')

    elif quantidade > 5 and tipo_da_carne == 'alcatra' and cartao == 'nao':
        preço_total = quantidade * 5.90
        desconto = 0
        print(f'=====CUPOM FISCAL=====\n Tipo da carne:     {tipo_da_carne}\n Preço total:     {preço_total}\nTipo de pagamento:     Dinheiro\n Valor do desconto:     {desconto}\n Preço a pagar:     {preço_total}')

    elif quantidade > 5 and tipo_da_carne == 'picanha' and cartao == 'nao':
        preço_total = quantidade * 6.90
        desconto = 0
        print(f'=====CUPOM FISCAL=====\n Tipo da carne:     {tipo_da_carne}\n Preço total:     {preço_total}\nTipo de pagamento:     Dinheiro\n Valor do desconto:     {desconto}\n Preço a pagar:     {preço_total}')
    
    elif quantidade > 5 and tipo_da_carne == 'file' and cartao == 'sim':
        preço_total = quantidade * 4.90
        desconto = preço_total * (5/100)
        valor_total = preço_total - desconto
        print(f'=====CUPOM FISCAL=====\n Tipo da carne:     {tipo_da_carne}\n Preço total:     {preço_total}\nTipo de pagamento:     Cartão\n Valor do desconto:     {desconto}\n Preço a pagar:     {valor_total}')

    elif quantidade > 5 and tipo_da_carne == 'alcatra' and cartao == 'sim':
        preço_total = quantidade * 5.90
        desconto = preço_total * (5/100)
        valor_total = preço_total - desconto
        print(f'=====CUPOM FISCAL=====\n Tipo da carne:     {tipo_da_carne}\n Preço total:     {preço_total}\nTipo de pagamento:     Cartão\n Valor do desconto:     {desconto}\n Preço a pagar:     {valor_total}')

    elif quantidade > 5 and tipo_da_carne == 'picanha' and cartao == 'sim':
        preço_total = quantidade * 6.90
        desconto = preço_total * (5/100)
        valor_total = preço_total - desconto
        print(f'=====CUPOM FISCAL=====\n Tipo da carne:     {tipo_da_carne}\n Preço total:     {preço_total}\nTipo de pagamento:     Cartão\n Valor do desconto:     {desconto}\n Preço a pagar:     {valor_total}')



main()
