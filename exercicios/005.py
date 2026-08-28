from math import pi  #Importa o valor de PI para o cálculo do círculo

print('-' * 45)
print('Cálculo de Área de Figuras Geométricas')
print('-' * 45)

print('''Escolha a figura: 
[ 1 ] Quadrado
[ 2 ] Retângulo
[ 3 ] Triângulo
[ 4 ] Círculo''')

opcao = int(input('Sua opção: '))

print('-' * 45)

# Cálculo para o Quadrado
# Multiplica lado por lado
if opcao == 1:
    lado = float(input('Digite o valor do lado: '))
    area = lado * lado
    print(f'Área do Quadrado: {area:.2f}')

# Cálculo para o Retângulo
# Base vezes altura
elif opcao == 2:
    base = float(input('Digite a base: '))
    altura = float(input('Digite a altura: '))
    area = base * altura
    print(f'Área do Retângulo: {area:.2f}')

# Cálculo para o Triângulo
# Base vezes altura dividido por 2
elif opcao == 3:
    base = float(input('Digite a base: '))
    altura = float(input('Digite a altura: '))
    area = (base * altura) / 2
    print(f'Área do Triângulo: {area:.2f}')

# Cálculo para o Círculo
# PI vezes o raio ao quadrado
elif opcao == 4:
    raio = float(input('Digite o raio: '))
    area = pi * (raio ** 2)
    print(f'Área do Círculo: {area:.2f}')

else:
    print('Opção inválida! Escolha de 1 a 4.')

print('-' * 45)
