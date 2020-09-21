senha = input('Digite a senha:')


if len(senha) < 6:
    print('Primeiramente sua senha deve conter mais de 6 (seis) caracteres.')


counter = 0

minusculas = 0
maisculas = 0
numeros = 0
especial = 0


for i in range(len(senha)):
    if ord(senha[i]) >= 65 and ord(senha[i]) <= 90:
        maisculas += 1 
    if ord(senha[i]) >= 97 and ord(senha[i]) <= 122:
        minusculas +=1
    if ord(senha[i]) >= 48 and ord(senha[i]) <= 57:
        numeros += 1
    if senha[i] == '!' or senha[i] == '@' or senha[i] ==  '#' or senha[i] ==  '$' or senha[i] == '%' or senha[i] == '^' or senha[i] == '&' or senha[i] == '*' or senha[i] == '(' or senha[i] == ')' or senha[i] == '-' or senha[i] == '+':
        especial += 1


if maisculas == 0:
    counter += 1
if minusculas == 0:
    counter += 1
if numeros == 0:
    counter += 1
if especial == 0:
    counter += 1


print(f'{counter} tipo(s) caractere(s) faltam para a sua senha ser forte!')