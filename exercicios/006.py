print('-' * 45)
print('Cálculo de Porcentagem')
print('-' * 45)

valor = float(input('Digite um valor: R$ '))
porcentagem = float(input('Qual seria a porcentagem? '))

# Cálculo da porcentagem
resultado = (valor * porcentagem / 100)

print('-' * 45)
print(f'{porcentagem}% de R${valor:.2f} é igual a R${resultado:.2f}')
print('-' * 45)
