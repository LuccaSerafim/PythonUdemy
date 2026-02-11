"""
Aula falando sobre *args (desempacotamento e empacotamento)

args são argumentos não nomeados.

O args nos retorna uma tuple, e diferentemente de uma lista, a tupla você não pode altera-la

No args a gente pode usar os acumuladores, que é uma variavel onde vamos somar ele mesmo + algo, e a cada iteração
ele vai salvando os valores.

Temos a propria função do python de soma que é a sum(), onde recebe iteraveis e so podemos passar 2 argumentos dentro

"""



def palavras(*args):
    return " ".join(args)

frase_pronta = palavras("Ola","Github!")
print(frase_pronta)


def multiplicar(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

numeros = [10,23, 54]
print(multiplicar(*numeros))