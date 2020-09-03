def main():

    palavra = str(input('Digite uma palavra: '))
    numero = int(input("Digite um número: "))


    for i in range(len(palavra)):
        if ord(palavra[i]) >= 65 and ord(palavra[i]) <= 90:
            num = ord(palavra[i]) + numero
            num__65 = num - 65 
            num__90 = num - 90
            if num < 65:
                num = 91 + num__65
                print(chr(num), end="")
                continue
            if num > 90:
                num = 64 + num__90
                print(chr(num), end="")
                continue
            if num >= 65 and num <= 90:
                print(chr(num), end="")
        elif ord(palavra[i]) >= 97 and ord(palavra[i]) <= 122:
            num1 = ord(palavra[i]) + numero
            num__97 = num1 - 97 
            num__122 = num1 - 122
            if num1 < 97:
                num1 = 123 + num__97
                print(chr(num1), end="")
                continue
            if num1 > 122:
                num1 = 96 + num__122
                print(chr(num1), end="")
                continue
            if num1 >= 97 and num1 <= 122:
                print(chr(num1), end="")



main()