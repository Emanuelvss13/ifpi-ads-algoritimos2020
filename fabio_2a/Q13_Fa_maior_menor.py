def main():
    
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    n3 = int(input('Digite o 3º número: '))
    n4 = int(input('Digite o 4º número: '))
    n5 = int(input('Digite o 5º número: '))

    maior_menor(n1, n2, n3, n4, n5)


def maior_menor(n1, n2, n3, n4, n5):
   if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
      print(f'O maior número é o {n1}', end = ' ')
   if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
      print(f'O maior número é o {n2}', end = ' ')
   if n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
      print(f'O maior número é o {n3}', end = ' ')
   if n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
      print(f'O maior número é o {n4}', end = ' ')
   if n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
      print(f'O maior número é o {n5}', end = ' ')
   if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
      print(f'e o menor é {n1}')
   if n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
      print(f'e o menor é {n2}')
   if n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
      print(f'e o menor é {n3}')
   if n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
      print(f'e o menor é {n4}')
   if n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
      print(f'e o menor é {n5}')

main() 



