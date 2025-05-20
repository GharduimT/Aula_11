# Programa que receba duas notas do aluno, calcule a média e informe se foi aprovado
# usar try para converter para float, except para tratar erro caso o usuário digite texto ou valor inválido
# usar else *caso não dê erro no try) para
#     verrificar se as notas estão no intervalo de 0 a 10 
#     calcular e exibir a media 
# informar se o aluno foi aprovado (media >= 6)
# Usar o finally para exibir uma mensagem de encerramento

while True:
    try:
        nota1 = int(input('Informe a primeira nota: '))
        if nota1 < 0 or nota1 > 10:
            print("A nota deve ser numérica e de 0 a 10 tente novamente")

            continue

        nota2 = int(input('Informe a segunda nota: '))
        if nota2 < 0 or nota2 > 10:
            print("A nota deve ser numérica e de 0 a 10 tente novamente")
            continue
        media = (nota1 + nota2)/2
        print(f'Média: {media}')
        # break

    except ValueError:
        print("Por favor, digite apenas números válidos.")
    else:
        if media >= 6:
            print('Aluno APROVADO. Sua média foi:', media)
        elif media <= 5:
            print('Aluno REPROVADO. Sua media foi:', media)
    finally:
        print('fim do programa')