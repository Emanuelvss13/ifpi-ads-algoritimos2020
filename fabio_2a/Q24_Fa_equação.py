from math import sqrt
def main():
    a = int(input('Digite o coeficiente A: '))
    b = int(input('Digite o coeficiente B: '))
    c = int(input('Digite o coeficiente C: '))

    equaçao(a, b, c)

def equaçao(a, b, c):
    delta = b ** 2 - 4 * a * c
    if a <= 0:
        print('O coeficiente A não pode ser menor ou igual que 0 (Zero).')
    elif delta < 0:
        print('O delta é menor que 0 (zero), não existe raiz real.')
    elif delta == 0:
        r = ((-b + sqrt(delta)) / (2 * a))
        print(f'O delta é igual a 0 (Zero), exite uma raiz e ela é {r}.')
    elif delta > 0:
        r_1 = ((-b + sqrt(delta)) / (2 * a))
        r_2 = ((-b - sqrt(delta)) / (2 * a))
        print(f'O delta é maior que 0 (Zero), exitem duas raizes e elas são {r_1} e {r_2}.')

main()