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
<summary><b>📄 001.py — Média Escolar e Situação do Aluno</b></summary>

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
