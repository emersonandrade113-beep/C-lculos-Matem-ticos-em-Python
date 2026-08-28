# 🧮 Cálculos Matemáticos em Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Algorithms-Lógica_de_Programação-007ACC?style=for-the-badge&logo=python&logoColor=white" alt="Algorithms" />
</p>

---

> *"Algoritmos e matemática na prática! Coleção de scripts em Python focados na resolução de problemas, manipulação numérica e desenvolvimento do raciocínio lógico."*

---

### 🧠 Sobre o Projeto

Este repositório reúne uma coleção de scripts e exercícios práticos desenvolvidos em **Python**, focando na resolução de problemas matemáticos, manipulação de dados numéricos e consolidação da lógica de programação.

---

### 📂 Exercícios e Códigos (Clique para expandir)

<details>
<summary><b>📄 <a href="https://github.com/emersonandrade113-beep/C-lculos-Matem-ticos-em-Python/blob/main/exercicios/001.py">001.py</a> — Média Escolar e Situação do Aluno</b></summary>

```python
# Recebendo as notas
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))

# Cálculo Média
media = (n1 + n2 + n3 + n4) / 4

# Lógica de aprovação
if media >= 7.0:
    print('O aluno está APROVADO.')

elif media >= 5.0:
    print('O aluno está de RECUPERAÇÃO.')

else:
    print('O aluno está REPROVADO.')

print(f'\nTirando {n1:.2f}, {n2:.2f}, {n3:.2f} e {n4:.2f}, a média do aluno é {media:.2f}')
Python
# Biblioteca para calcular o Fatorial
from math import factorial

n = int(input('Digite um número para calcular seu Fatorial:'))

# Aqui serve apenas para validar números negativos
if n < 0:
    print('Não existe fatorial de número negativo.')
    
else:
    f = factorial(n)
    print(f'O fatorial de {n}! é {f}')
Python
print('-' * 45)
print('Conversor de temperatura')
print('-' * 45)

print('''Escolha a conversão: 
[ 1 ] Celsius para Fahrenheit
[ 2 ] Fahrenheit para Celsius''')

# Escolhe qual tipo de conversão deseja
opcao = int(input('Sua opção: '))

if opcao == 1:
    # Recebe a temperatura em Celsius
    c = float(input('Informe a temperatura de °C: '))
    
    # Converte Celsius para Fahrenheit
    f = (c * 1.8) + 32
    
    print(f'A temperatura de {c}°C corresponde a {f:.1f}°F!')

elif opcao == 2:
    # Recebe a temperatura em Fahrenheit
    f = float(input('Informe a temperatura de °F: '))
    
    # Converte Fahrenheit para Celsius
    c = (f - 32) / 1.8
    
    print(f'\nA temperatura de {f}°F corresponde a {c:.1f}°C!')
    
else:
    # Caso o usuário digite uma opção inválida
    print('Opção inválida! Tente novamente.')

print('-' * 45)
Python
print('''Escolha a conversão: 
[ 1 ] Quilômetros para Metros
[ 2 ] Metros para Centímetros
[ 3 ] Horas para Minutos''')

# Escolhe qual conversão quer fazer
opcao = int(input('Sua opção: '))

if opcao == 1:
    km = float(input('Digite quantos quilômetros: '))
    # Converte km para metros (1 km = 1000 metros)
    metros = km * 1000
    print(f'{km:.2f} km correspondem a {metros:.2f} metros.')

elif opcao == 2:
    m = float(input('Digite quantos metros: '))
    # Converte metros para centímetros (1 metro = 100 cm)
    centimetros = m * 100
    print(f'{m:.2f} metros correspondem a {centimetros:.0f} centímetros.')

elif opcao == 3:
    h = float(input('Informe as horas: '))
    # Converte horas para minutos (1 hora = 60 minutos)
    minutos = h * 60
    print(f'{h:.2f} horas correspondem a {minutos:.0f} minutos.')

else:
    # Caso o usuário digite uma opção errada
    print('Opção inválida! Escolha entre 1, 2 ou 3.')
Python
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
if opcao == 1:
    lado = float(input('Digite o valor do lado: '))
    area = lado * lado
    print(f'Área do Quadrado: {area:.2f}')

# Cálculo para o Retângulo
elif opcao == 2:
    base = float(input('Digite a base: '))
    altura = float(input('Digite a altura: '))
    area = base * altura
    print(f'Área do Retângulo: {area:.2f}')

# Cálculo para o Triângulo
elif opcao == 3:
    base = float(input('Digite a base: '))
    altura = float(input('Digite a altura: '))
    area = (base * altura) / 2
    print(f'Área do Triângulo: {area:.2f}')

# Cálculo para o Círculo
elif opcao == 4:
    raio = float(input('Digite o raio: '))
    area = pi * (raio ** 2)
    print(f'Área do Círculo: {area:.2f}')

else:
    print('Opção inválida! Escolha de 1 a 4.')

print('-' * 45)
Python
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
