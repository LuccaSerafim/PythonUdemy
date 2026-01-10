# Exercicio de Calculadora com While
# Na documentação do python o .lower() retorna em letras minusculas o que foi atribuido a ele.
# Temos tambem a .startswith() que no caso quer saber se uma string começa com alguma letra(retorna bool)
# E o .endswith que quer saber se termina com determinada letra(retorna bool)


# Meu codigo
while True:
    num_1 = float(input("Digite um número: "))
    num_2 = float(input("Digite outro número: "))
    operadores = input("Escolha um operador (+ ; - ; * ; /): ")

    SOMA = num_1 + num_2
    SUBTRACAO = num_1 - num_2
    MULTIPLICACAO = num_1 * num_2
    DIVISAO = num_1 / num_2
    
    if operadores == "+":
        print(SOMA)

    elif operadores == "-":
        print(SUBTRACAO)

    elif operadores == "*":
        print(f"{MULTIPLICACAO:.2f}")

    elif operadores == "/":
        if num_1 == 0 or num_2 == 0:
            print("Não é possivel dividir por zero")
            continue
        print(f"{DIVISAO:.2f}")

    else: 
        print("Você escolheu uma operação inexistente.")
        continue



    sair = input("Você quer sair? [s]im [n]ão:  ").lower().startswith("s")
    

    if sair:
        break
    
# Lembrando que para usar o :.2f usa a f-string
# O continue ele volta pro começo do laço e roda novamente.

    
    
    





