# Biblioteca para calcular o Fatorial
from math import factorial

n = int(input('Digite um número para calcular seu Fatorial:'))

# Aqui serve apenas para validar números negativos
if n < 0:
    print('Não existe fatorial de número negativo.')
    
else:
    f = factorial(n)
    print(f'O fatorial de {n}! é {f}')
