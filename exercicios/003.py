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
