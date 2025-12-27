# Exercicio usando operadores relacionais e condicionais tbm
# Queremos que o usuario me de 2 valores, se o 1 valor for maior aparece na tela que o primeiro e maior que o segundo e vice-versa
# Por eu ter pensado dms tinha a possibilidade de eu eliminar o ultimo elif onde eu disse que são igual e trocar por um else
# Exemplo: else: print("Os valores que você digitou são igual. Por favor escreva valores diferentes")

valor1 = input("Digite um Valor(Número): ")
valor2 = input("Digite outro Valor(Número): ")

valor_correto1  = float(valor1)
valor_correto2 = float(valor2)

if valor_correto1 > valor_correto2:
    print(f'O 1° valor = {valor_correto1:.2f} é maior que o 2° valor = {valor_correto2:.2f} ')

elif valor_correto2 > valor_correto1:
    print(f"O 2° valor = {valor_correto2:.2f} é maior que o 1° valor = {valor_correto1:.2f} ")

elif valor_correto1 == valor_correto2:
        print("Os valores que você digitou são igual. Por favor escreva valores diferentes")


