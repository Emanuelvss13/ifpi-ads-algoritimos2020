def main():
    q_ma = float(input('Digite quantos Kg de maça foram comprados: '))
    q_mo = float(input('Digite quantos Kg de morango foram comprados: '))

    frutas(q_ma, q_mo)

def frutas(q_ma, q_mo):
    if q_ma <= 5 and q_mo <= 5:
        valor_ma = q_ma * 1.80
        valor_mo = q_mo * 2.50
        valor_t = valor_ma + valor_mo
        print(f'Você ira pagar R${valor_t}')
    
    elif q_ma >= 5 and q_mo >= 5:
        valor_ma = q_ma * 1.50
        valor_mo = q_mo * 2.20
        valor_t = valor_ma + valor_mo
        print(f'Você ira pagar R${valor_t}')

    elif q_ma > 5 and q_mo <= 5:
        valor_ma = q_ma * 1.50
        valor_mo = q_mo * 2.50
        valor_t = valor_ma + valor_mo
        print(f'Você ira pagar R${valor_t}')
    
    elif q_ma <= 5 and q_mo > 5:
        valor_ma = q_ma * 1.80
        valor_mo = q_mo * 2.20
        valor_t = valor_ma + valor_mo
        print(f'Você ira pagar R${valor_t}')

    if (q_ma + q_mo) > 8 or valor_t > 25:
        valor_do_desconto = valor_t * (10/100)
        valor_c_desconto = valor_t - valor_do_desconto
        print(f'Mas o valor com desconto é R$ {valor_c_desconto}')


main()

