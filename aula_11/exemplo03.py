try: 
    n1 = float(input('Numero: '))
    n2 = float(input('Numero: '))
    resultado = n1 / n2

    
except ZeroDivisionError as e:
    print(f'Não há divisão por 0 - {e}')

else:
    print(f'O resultado é: {resultado}')

            
finally:
    print('Fim da Operação!')