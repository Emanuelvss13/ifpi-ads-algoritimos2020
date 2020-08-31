n_parada = 1

for i in range(10000000):
    salario = 0
    inss = 0
    ir = 0
    
    nome_funcionario = str(input('Digite o codigo do funcionário: '))
    horas_trabalhadas = float(input('Digite quantas horas ele trabalhou: '))
    dependentes = int(input('Digite quantos dependentes o funcionario tem: '))
    

    salario_bruto = (horas_trabalhadas * 12) + (dependentes * 40)
    inss = salario_bruto / 100 * 8.5
    ir = salario_bruto / 100 * 5
    descontos = inss + ir
    salario_liquido = salario_bruto - descontos

    print(f'O valor pago no inns é: R${inss}')
    print(f'O valor pago no imposto de renda é: R${ir}')
    print(f'O salário liquido é: R${salario_liquido}')
    n_parada = int(input('Digite 1 para pesquisar outro funcionário, para sair digite qualquer tecla.: '))

    if n_parada != 1:
        break

