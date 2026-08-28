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
