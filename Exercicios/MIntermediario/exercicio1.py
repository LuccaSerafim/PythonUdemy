"""
1° Exercício do Módulo Intermediário: Funções.

Cria uma função que multiplique todos os argumentos não nomeados recebidos, retorne o total para uma variavel
e mostre o valor da variavel

Crie uma função que fala se é impar ou par, retorne se o numero é par ou impar.

"""

def multiplicacao(*args):
    total = 1
    for numeros in args:
        total *= numeros

    return total

teste_num = multiplicacao(3, 3, 14, 10)
print(teste_num)


def par_ou_impar(numeros):
    
    if numeros % 2 == 0:
        return f"O número {numeros} é par"

    return f"O número {numeros} é impar"

    
verificando_numero = par_ou_impar(180)
print(verificando_numero)