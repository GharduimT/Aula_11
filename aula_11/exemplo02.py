# try: #  TENTE EXECUTAR

#     n1 = float(input('Numero: '))
#     n2 = float(input('Numero: '))
#     div = n1 / n2
#     print(div)
    
# except ZeroDivisionError:  #  escreva a mensagem ERROR se tentar dividir por zero
#     print('Error')

# #2
# try: 
#     n1 = float(input('Numero: '))
#     n2 = float(input('Numero: '))
#     div = n1 / n2
#     print(div)
    
# except ZeroDivisionError as e: 
#     print(f'Não pode dividir por 0 - {e}')

#3
# try: 
#     n1 = float(input('Numero: '))
#     n2 = float(input('Numero: '))
#     div = n1 / n2
#     print(div)
    
# except ZeroDivisionError as e: 
#     print(f'Não pode dividir por 0 - {e}')

# except ValueError as e:
#     print(f'Não digite por extenso - {e}')

try: 
    n1 = float(input('Numero: '))
    n2 = float(input('Numero: '))
    div = n1 / n2
    print(div)
    
except (ValueError, TypeError) as e: 
    print(f'Informe apenas números - {e}')

except ZeroDivisionError as e:
    print(f'Não há divisão por 0 - {e}')