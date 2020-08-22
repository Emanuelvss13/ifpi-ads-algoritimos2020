n_parada = 1

boi_magro = 10000000
boi_gordo = 0

while n_parada == 1:
    indentificação_boi = str(input('Digite o numero de indentificação do boi: '))
    peso_boi = float(input('Digite o peso do boi em KG: '))
    n_parada  = int(input('Digite um (1) para adicionar outro boi: '))
    
    if peso_boi < boi_magro:
        boi_magro = peso_boi
        numero = indentificação_boi
    
    if peso_boi > boi_gordo:
        boi_gordo = peso_boi
        numero1 = indentificação_boi
    
    

print(f'Boi mais gordo: nº de indetificação - {numero1}, peso: {boi_gordo} Kg')
print(f'Boi mais magro: nº de indetificação - {numero}, peso: {boi_magro} Kg')

