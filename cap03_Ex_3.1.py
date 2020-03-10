def right_justify(s):
    espaços = 70 - len(s)
    texto = (' ' * espaços) + s 
    print(texto)    

right_justify('monthy')