"""
Aula introdutoria a listas mutaveis em python: List
Temos duas formas de criar uma lista com o list. 1° é a propia função list() (geralmente usada caso queremos
fazer uma coerção de tipo) e a 2° é criar uma variavel qualquer e igualar a []. Ex: lista = [].

A lista suporta vários valores de qualquer tipo.
Podemos ter listas dentro de listas.


Podemos fazer um type(lista) onde retorna para nós o tipo list. O list por ser mutavel eu posso acessar um indice
de algo e mudar aquele indice, diferentemente dos tipos imutaveis.

Uma lista vazia retorna para nós False se fizermos a coerção para bool().

Diferentemente de uma string onde acessarmos um caractere de cada vez, na lista a gente acessa o elemento completo,
onde se tivermos uma lista com varias coisas separadas por , cada coisa vai ser um valor inteiro.
EXString: nome = "Lucca" , print(nome[2]). Isso nos retorna apenas o caracter c. 
ExLista: lista = ["Lucca", 20, 1.82] print(lista[0]). Isso me retorna "Lucca" completo assim e não apenas o 1° 
caractere

Por uma coisa estar dentro de uma lista, a gente pode usar os conhecimentos que vimos ja nas coisas da lista normalmente,
pelo fato de estar dentro nao muda nada.

Agora podemos alterar de fato uma string caso queremos. EX: lista[-3] = "Cleiton". Isso me diz que o interprador vai
vai no indice -3 (ou 0) e vai mudar de lucca para cleiton, e quando dermos o print ele vai mudar direto na lista.
So lembrando que indices + começam no 0(se refere ao primeiro indice) e 
os - começam em -1(Onde o -1 se refere ao ultimo indice).

Lista tem os indices + e - normais. 



"""
nome = "Lucca" 
print(nome[2])
lista = ["Lucca", 20, 1.82]
lista[-3] = "Cleiton"
print(lista[0])
