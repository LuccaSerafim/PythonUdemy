"""
Aula falando sobre as Funções de Primeira Ordem (High Order Functions)

High Order Functios = Funções que podem receber e/ou retornar outras funções

Funções podemos fazer varias coisas com ela, como por exemplo, crirar uma função com um argumento,
criar outra função e chamar esse argumento.

Sendo bem sincero, não entendi muito bem essa aula, por isso vou so colar o código do professor abaixo:
"""
def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)