"""
Aula falando sobre o tipo de dado Dict (Dicionarios em python) que tem a estrutura de dados do tipo
par de "chave" e "valor". 

A chave pode ser considerado como indices e o valor é o valor em si.

As chaves são criadas com tipos imutaveis. Ja o valor pode ser de qualquer tipo, ate mesmo outro dicionario.

Usamos as {} para criar um dicionario ou tambem a classe dict().

OBS: Se criarmos um dicionario com {}, passamos o argumento com dois pontos(:), agora se criarmos com
dict() passamos o argumento com sinal de igual(=)
EXOBS: teste = {
    "mensagem": "Olá"}

teste1 = dict(mensagem= "Olá")

Agora suponha que a gente tem varios argumentos no nosso dicionario, ai para acessar a gente usa o nome do 
dicionario junto com os []. Mesma coisa que um indice de uma lista 

Ex: print(teste["mensagem"])

So relembrando o que mutavel e imutavel que vimos:

Imutaveis = string, bool, int, float e tupla (tuple)
Mutaveis = list (listas) e dict(dicionarios)


Usamos os dicionarios na programação basicamente igual na vida real, para acharmos um valor de um indice
onde esse indice vai ser referenciado mais facilmente.


"""

dicionario_teste = {
    "pessoa": "cleiton",
    "idade": 33,
    "cidade": "Amapa",
    "telefones" : [
        {99: "xXXXX-XXXx", 
         43: "XXXXX-XXXX"}
    ]
}

print(dicionario_teste["pessoa"])
