"""
Aula sobre função Lambda. É uma função como qualquer outra no python, porém
geralmente é uma função de uma linha.

Ou seja, tudo deve conter dentro de uma unica expressão.

Se usa chamando o própio lambda, seguida de argumentos, dois-pontos (:) e uma expressão que é avaliada e retornada automaticamente
Ex: lambda argumentos: expressão

São ideais para operações rápidas e temporárias onde você passaria uma função simples como argumento para outra função.

OBS que nao tem a ver com a aula de lambda em si, no python temos função .sort da lista, onde ela ordena a lista original
e temos a sorted(), onde dentro desses () ele ira criar uma outra lista baseada na original mas ordenar ela.

"""
# Irei usar o código do professor, porém fazendo os comentários correspondentes


# nossa lista padrão do código juntamente com um dict(dicionário) dentro
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# função onde vai percorrer nossa lista item por item e imprimir na ordem que está padrão
def exibir(lista):
    for item in lista:
        print(item)
    print()

# aqui vamos criar 2 listas baseadas na padrão, isso que o .sorted() faz. Além de passarmos nosso argumento com o lambda que nesse caso vai ser o item
# e a "expressão" que vamos avaliar vai ser o nome na lista1 e o sobrenome na lista2
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)