print('=== AGIOT BANK ===')

try:
    saldo = 1000
    saque = float(input('Infomre o Valor para saque: '))

except ValueError as e:
    print(f'Digite apenas números: {e}')