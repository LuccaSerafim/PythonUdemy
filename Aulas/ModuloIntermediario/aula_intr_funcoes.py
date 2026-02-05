"""
1° Aula do Módulo Intermediário

Vamos fazer uma introdução as funções (def).

Geralmente as funções que a gente cria com o def são usadas em vários trechos de código para replicar
determinada ação.

A gente define essa função com def e um nome que a gente quiser(geralmente em minusculo), com () e : no final.
Ex: def numeros():

Elas podem receber valores para parametros(argumentos) e retornar um valor especifico.
Por padrão, as funções retornam um None(não valor)

Ex: def numeros(a, b, c):

OBS1: os parametros é o que a gente define aqui () quando criamos a função, imaginamos eles como variaveis, já os
argumentos seriam os valores dessas variaveis.

OBS2: se a gente chamar nossa função numeros sem passar nada. Só assim: numeros(), vai dar erro falando que esta
faltando os argumentos que a gente definiu, no caso foram 3. Porém, se a gente definir o argumento dentro do (), 
ai podemos chamar ela sem nada.

Ex: def numeros(a = "Nada"):
    print(f" Nossos numeros são = {a}")

numeros()


Podemos mudar os argumentos quando fizermos a chamada das funções.

So mostrando que podemos ter várias coisas dentro da função que a gente criou, exemplo esta no fim do código!

"""


def numeros(a = "Nada"):
    print(f" Nossos numeros são = {a}")

numeros(1)
numeros(10)
numeros()
numeros(10000)


# Código de exemplo do teste da plataforma:

# def multiplo_de(numero, multiplo):
#     resultado = numero % multiplo == 0
#     print(f'{numero} é múltiplo de {multiplo}?', end=' ')
#     print(resultado)
 
 
# multiplo_de(16, 8)
# multiplo_de(15, 3)
# multiplo_de(10, 2)