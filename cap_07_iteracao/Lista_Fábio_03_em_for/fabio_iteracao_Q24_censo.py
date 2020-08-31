habitantes = 1
salario_total = 0
total_filhos = 0
acima_mil = 0

for i in range(100000000000):

    salario = int(input('Digite o salario do habitante: '))
    n_filhos = int(input('Digite o numero de filhos: '))
    n_parada = int(input('Digite 1 para adicionar outro habitante: '))
    if n_parada != 1:
        if salario > 1000:
            acima_mil += 1
        salario_total += salario
        media_salario = salario_total / habitantes
        total_filhos += n_filhos
        media_filhos = total_filhos / habitantes
        percentual = acima_mil * (100 / habitantes)
        break
    else:
        if salario > 1000:
            acima_mil += 1
        salario_total += salario
        media_salario = salario_total / habitantes
        total_filhos += n_filhos
        media_filhos = total_filhos / habitantes
        percentual = habitantes * (acima_mil/100)
        habitantes += 1
        



print(f'O numero de habitantes cadastrados é: {habitantes}')
print(f'A média sálarial é de: {"%.2f" % media_salario}')
print(f'A média de filhos é: {"%.2f" % media_filhos}')
print(f'O percentual de pessoas que ganham mais de R$1000 é: {"%.2f" % percentual}%')


