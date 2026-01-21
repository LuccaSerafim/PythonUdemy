"""
Aula mostrando como concatenar e extender listas

Relembrando os metodos:

append - Adiciona um item ao final
insert - Adiciona um item no índice escolhido
pop - Remove do final ou do índice escolhido
del - apaga um índice
clear - limpa a lista
extend - estende a lista
+ - concatena lista

Para juntarmos uma lista na outra temos as 2 opções: Concatenar e o Extend

A concatenação é igual que vimos anteriormente. Voce pega a variavel que tem uma lista, pega a outra variavel 
e usa o sinal de + para juntar os valores das duas listas em uma outra variavel.
Ex: lista1 = ["a, b, c"] | lista2 = ["d, e, f"] | listaconcatenada = lista1 + lista2
print(listaconcatenada)

Agora para o extend tem algumas observações. 1° que o extend é uma função: .extend()
2° voce não pode pegar uma outra variavel e usar o extend na variavel criada pois a função retorna None
Ex que nao deve fazer: listaextendida = lista1.extend(lista2) | print(listaextendida) vai retorna None.
Ele retorna none pois o extend mexe diretamente no valor da lista que vc esta extendendo, no caso desse exemplo a 
lista1.
O correto seria só: lista1.extend(lista2) | print(lista1)



"""

lista1 = ["a, b, c"] 
lista2 = ["d, e, f"] 
listaconcatenada = lista1 + lista2
print(listaconcatenada)
lista1.extend(lista2)
print(lista1)