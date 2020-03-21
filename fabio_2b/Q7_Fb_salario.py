def main():
    salario = float(input('Digite seu salário: '))

    aumento(salario)

def aumento(salario):
    if salario <= 280:
        valor_do_aumento = salario * (20/100)
        novo_salario = salario + valor_do_aumento
        print(f'Seu salário era de {salario}, o percentual de aumento foi de 20%, com isso seu salário aumento em {valor_do_aumento} e passou a ser de {novo_salario}')
    
    elif salario > 280 and salario <= 700:
        valor_do_aumento = salario * (15/100)
        novo_salario = salario + valor_do_aumento
        print(f'Seu salário era de {salario}, o percentual de aumento foi de 15%, com isso seu salário aumento em {valor_do_aumento} e passou a ser de {novo_salario}')
    
    elif salario > 700 and salario <= 1500:
        valor_do_aumento = salario * (10/100)
        novo_salario = salario + valor_do_aumento
        print(f'Seu salário era de {salario}, o percentual de aumento foi de 10%, com isso seu salário aumento em {valor_do_aumento} e passou a ser de {novo_salario}')
    
    elif salario > 1500:
        valor_do_aumento = salario * (5/100)
        novo_salario = salario + valor_do_aumento
        print(f'Seu salário era de {salario}, o percentual de aumento foi de 5%, com isso seu salário aumento em {valor_do_aumento} e passou a ser de {novo_salario}')
    
main()