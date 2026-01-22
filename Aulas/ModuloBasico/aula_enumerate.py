"""
Aula falando sobre o método enumerate().

Serve para enumerar iteráveis (indices)

O enumerate é um iterator, ou seja, caso quisermos podemos usar o next() para ir pegando valor por valor.

Geralmente o enumerate a gente não usa com uma variavel e sim geralmente em um for por exemplo.
Porem caso a gente use o enumerate com uma variavel é bom fazer a coerção para lista ou tupla.

Uma curiosidade: o "\t" da um tab igual como o "\n" quebra a linha

"""

# Poderiamos ter usado o enumerate no exercicio 7:

lista = ["Maria", "Luiz", "João", "Kleber"]

for indices in enumerate(lista):
    print(indices, end="")