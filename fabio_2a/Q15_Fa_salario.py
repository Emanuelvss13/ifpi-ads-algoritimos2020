def main():
    h1 = float(input('Digite quantas horas trabalha o 1º professor:'))
    h2 = float(input('Digite quantas horas trabalha o 2º professor:'))
    s1 = float(input('Digite quanto ganha por hora o 1º professor: '))
    s2 = float(input('Digite quanto ganha por hora o 2º professor: '))

    resultado = salario(h1, h2, s1, s2)

    print(resultado)

def salario(h1, h2, s1, s2):
    p1 = h1 * s1
    p2 = h2 * s2
    if p1 > p2:
        return f'O maior sálario é o do 1º professor.'
    else:
        return f'O maior sálario é o do 2º professor.'

main()