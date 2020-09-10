palavra = str(input('Digite um palavra para ser criptografada: '))


for i in range(len(palavra)-1 , -1, -1):
    if ord(palavra[i]) >= 65 and ord(palavra[i]) <= 90 or ord(palavra[i]) >= 97 and ord(palavra[i]) <= 122:
        num = ord(palavra[i]) + 3
        mun = len(palavra) // 2
        if i <= mun:
            num -= 1
            print(chr(num), end="")
        else:
            print(chr(num), end="")
        continue
    print(palavra[i], end="")
    