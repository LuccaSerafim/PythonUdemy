"""
Aula falando sobre os cuidados que temos que ter com dados Mutaveis e falando sobre o metodo Copy

= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)

Relembrando os tipos Imutaveis que vimos até então: Strings, Int, Float e Bool

Já o metodo copy() e para realmente pegar um valor de uma lista e copiar ela em outra variavel
"""

# Código do professor pois tive preguiça

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)