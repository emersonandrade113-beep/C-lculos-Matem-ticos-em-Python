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
