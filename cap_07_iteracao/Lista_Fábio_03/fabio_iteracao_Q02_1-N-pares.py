def main():
    n = int(input('Digite um numero: '))

    comeco = 0

    while n >= comeco:
        
        if comeco % 2 != 0:
            comeco += 1
            continue
        else:
            print(comeco)
            comeco += 1

        


main()