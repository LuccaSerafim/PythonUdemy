"""
Aula onde vamos ver como inserir itens em qualquer indice da nossa lista (tipo list) com o insert

Relembrando os metodos:

append - Adiciona um item ao final
insert - Adiciona um item no índice escolhido
pop - Remove do final ou do índice escolhido
del - apaga um índice
clear - limpa a lista
extend - estende a lista(iremos ver em outra aula)
+ - concatena lista(iremos ver em outra aula)

O metodo insert vai ser o primeiro que vamos ver que precisamos passar 2 argumentos para ele funcionar. O 1° é 
em qual indice vamos adicionar e o 2° o valor que vamos adicionar.

Ex: lista = ["a", "b", "c", "d", "e"]. Suponha que eu quero adicionar um "z" no indice 2 (lugar onde o c esta)
Fazemos assim: lista.insert(2, "z")

OBS: Se fizermos um insert para um indice que não tem na nossa lista, o python ate faz esse insert porem
ele vai adicionar no ultimo indice da nossa lista. E se por acaso fizermos um print e queremos acessar esse indice
que não tem na nossa lista que a gente pediu no insert vai gerar um indexerror, que vai mostrar que esse indice
esta fora do range da nossa lista.
Ex: lista.insert(100, "100°")
Ele vai acabar adicionando esse "100°" no fim da nossa lista e se quisermos acessar o indice 100, vai gerar o erro.



"""
lista = ["a", "b", "c", "d", "e"]
lista.insert(100, "100°")
lista.insert(2, "z")
print(lista)