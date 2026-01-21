"""
Aula onde vamos aprender em como alterar uma lista com funções.

Temos o metodo CRUD para listas.
O CRUD significa: Create, Read, Update, Delete. E usando eles temos uma lista.

Na lista é interessante adicionar coisas, e deletar coisas do final dela, para assim evitar de movimentar ela demais,
pois isso gasta tempo de processamento.(Exemplo para listas muito grandes, se for pequena pode movimentar)

Métodos uteis das funções:
append, insert, pop, del, clear, extend, +...

o metodo "del" deleta um indice por exemplo da lista e por ter apagado, o proprio interpretador acaba reorganizando
os itens da lista.

Ex: lista = [10, 55, 101, "eu", "cachorro"]
print(lista[3]) . Retorna para mim o "eu"
ai se eu usar del lista[3] ele apaga o "eu" e se eu fizer de novo print(lista[3]) ele vai reorganizar a lista
e vai me retornar "cachorro"

O metodo "append" adiciona coisas ao final da nossa lista. Podemos fazer vários append
Ex: lista.append("oi") , caso dermos o print ele vai adicionar o "oi" no fim da nossa lista

O metodo "pop" remove o ultimo elemento da lista. Porém podemos remover um elemento atraves do indice dele
Ex: lista.pop() . lista.pop(2)

"""
lista = [10, 55, 101, "eu", "cachorro"]
lista.append("oi")
print(lista)
lista.pop()
lista.pop(2)
print(lista)
# print(lista[3])
# del lista[3]
# print(lista)
# print(lista[3])

