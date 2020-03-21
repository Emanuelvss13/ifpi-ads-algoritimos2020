def main():
    s = int(input("Digite a senha: "))

    senha(s)

def senha(s):
    if s == 1234:
        print('==============================')
        print('       ACESSO CONCEDIDO')
        print('==============================')    
    else:
        print('=============================')
        print('        ACESSO NEGADO')
        print('=============================')
    
main()