def main():
    n = int(input('Digite um número menor que 1000: '))

    c_d_u(n)

def c_d_u(n):
    if n >= 1000:
        print('Digite apenas números menores que 1000 :(')
    
    elif n > 99:
        centena = n // 100
        dezena = (n%100) // 10
        unidade = ((n%100)%10)

        if centena == 1:
            print(f'{centena} centena, {dezena} dezenas e {unidade} unidades')

        elif dezena == 1:
            print(f'{centena} centenas, {dezena} dezena e {unidade} unidades')

        elif unidade == 1:
            print(f'{centena} centenas, {dezena} dezenas e {unidade} unidade')

        elif centena == 1 and dezena == 1 and unidade == 1:
            print(f'{centena} centena, {dezena} dezena e {unidade} unidade')
    
        elif centena == 1 and dezena == 1:
            print(f'{centena} centena, {dezena} dezena e {unidade} unidades')

        elif centena == 1 and unidade == 1:
            print(f'{centena} centena, {dezena} dezenas e {unidade} unidade')

        elif dezena == 1 and unidade == 1:
            print(f'{centena} centenas, {dezena} dezena e {unidade} unidade')

        elif centena != 1 and dezena != 1 and unidade !=1:
            print(f'{centena} centenas, {dezena} dezenas e {unidade} unidades')

    
    
    elif n <= 99:
        centena = n // 100
        dezena = (n%100) // 10
        unidade = ((n%100)%10)


        if dezena == 1:
            print(f'{dezena} dezena e {unidade} unidades')

        elif unidade == 1:
            print(f'{dezena} dezenas e {unidade} unidade')

        elif dezena == 1 and unidade == 1:
            print(f'{centena} centena, {dezena} dezena e {unidade} unidade')

        elif dezena != 1 and centena != 1:
            print(f'{dezena} dezenas e {unidade} unidades')

    else:
        print('0 dezenas')

main() 