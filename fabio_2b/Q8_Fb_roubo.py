def main():
    v_h = float(input('Digite quanto você ganha por hora: '))
    t_h = int(input('Digite quantas horas você trabalhou no mês: '))

    impostos(v_h, t_h)

def impostos(v_h, t_h):
    salario_bruto = v_h * t_h
    if salario_bruto <= 900:
        i_r = 0
        inss  = salario_bruto * (10/100)
        fgts = salario_bruto * (11/100)
        total_desconto = i_r + inss
        salario_liquido = salario_bruto - i_r - inss
        print(f'Salário Bruto ({v_h} * {t_h})     : R$ {salario_bruto}')
        print(f'(-) IR (isento)            : R$ {i_r}')
        print(f'(-) INSS (10%)          : R$ {inss}')
        print(f'FGTS (11%)                : R$ {fgts}')
        print(f'Total de descontos        : R$ {total_desconto}')
        print(f'Salário Liquido         : R$ {salario_liquido}')
    
    elif salario_bruto > 900 and salario_bruto <= 1500:
        i_r = salario_bruto  * (5/100)
        inss  = salario_bruto * (10/100)
        fgts = salario_bruto * (11/100)
        total_desconto = i_r + inss
        salario_liquido = salario_bruto - i_r - inss
        print(f'Salário Bruto ({v_h} * {t_h})     : R$ {salario_bruto}')
        print(f'(-) IR (5%)            : R$ {i_r}')
        print(f'(-) INSS (10%)          : R$ {inss}')
        print(f'FGTS (11%)                : R$ {fgts}')
        print(f'Total de descontos        : R$ {total_desconto}')
        print(f'Salário Liquido         : R$ {salario_liquido}')

    elif salario_bruto > 1500 and salario_bruto <= 2500:
        i_r = salario_bruto  * (10/100)
        inss  = salario_bruto * (10/100)
        fgts = salario_bruto * (11/100)
        total_desconto = i_r + inss
        salario_liquido = salario_bruto - i_r - inss
        print(f'Salário Bruto ({v_h} * {t_h})     : R$ {salario_bruto}')
        print(f'(-) IR (10%)            : R$ {i_r}')
        print(f'(-) INSS (10%)          : R$ {inss}')
        print(f'FGTS (11%)                : R$ {fgts}')
        print(f'Total de descontos        : R$ {total_desconto}')
        print(f'Salário Liquido         : R$ {salario_liquido}')

    elif salario_bruto > 2500:
        i_r = salario_bruto  * (20/100)
        inss  = salario_bruto * (10/100)
        fgts = salario_bruto * (11/100)
        total_desconto = i_r + inss
        salario_liquido = salario_bruto - i_r - inss
        print(f'Salário Bruto ({v_h} * {t_h})     : R$ {salario_bruto}')
        print(f'(-) IR (20%)            : R$ {i_r}')
        print(f'(-) INSS (10%)          : R$ {inss}')
        print(f'FGTS (11%)                : R$ {fgts}')
        print(f'Total de descontos        : R$ {total_desconto}')
        print(f'Salário Liquido         : R$ {salario_liquido}')


main()