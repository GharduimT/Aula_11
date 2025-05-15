print('=== AGIOT BANK ===')

try:
    saldo = 1000
    saque = float(input('Infomre o Valor para saque: '))

except ValueError as e:
    print(f'Digite apenas números: {e}')


else:
    if saque < 0:
        if saldo >= saque:
            saldo -= saque
        elif saque > saldo:
            print('SALDO INSUFICIENTE')
        else:
            print('O saque precisa ser maior que 0')

finally:
    print('Operação finalizada!')
# saldo_fl = saldo - saque
# print(f'Restam {saldo_fl} reais em sua conta')
