def main():
    l = input('Digite uma letra: ')
    
    vog_con(l)

def vog_con(l):
    if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
        print(f'A letra {l} é uma vogal.')
    else:
        print(f'A letra {l} é uma consoante.')


main()