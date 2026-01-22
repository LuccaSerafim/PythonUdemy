"""
Exercicio 7: Exibir os indices da lista (Exercicio com solução na propia aula)

No caso ele deu uma lista com nomes e pediu para imprimir os indices deles junto com os nomes

"""
# Meu código:

lista = ["Maria", "Luiz", "João", "Kleber"]

for indices in  range(len(lista)):

    print(indices, lista[indices])
 
# Lembrete para lembrar do range e tambem que podemos usar as [] para botar as variaveis dentro e pegar os indices.

# Código Professor:

# lista = ['Maria', 'Helena', 'Luiz']
# lista.append('João')


# indices = range(len(lista))

# for indice in indices:
#     print(indice, lista[indice], type(lista[indice]))