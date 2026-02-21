"""
Aula falando sobre shallow copy e deep copy em dados mutaveis (listas e dicionarios. Ate entao vistos!)

OBS: Aula que acompanha as aulas dos metodos uteis dos Dicionarios!!!!

OBS2: Ao igualar dados mutaveis que vimos ate entao (list e dicts) voce esta apontando pro mesmo objeto na memoria
e não apenas igualando os valores. Se voce modificar um valor em 1 o outro vai ser modificado tbm.
EX: lista1 = ["Batata", "Arroz"]
lista2 = lista1
lista2.append("Feijao")

print(lista1) . Isso que eu fiz funciona para os Dicionarios tbm!!!!.

Partindo pra aula mesmo. Temos esses métodos abaixo:
copy = retorna uma copia rasa (shallow copy).Se usa com .copy() .Ele faz uma copia de tudo que for IMUTAVEL e 
cria um dicionario independente. 

Ex: dicionario1 = {
        "nome": "Cleiton",
        "idade": 21,

}

dicionario2 = dicionario1.copy()
dicionario2["nome"] = "João Paulo"

print(dicionario1)
print(dicionario2). Aqui ficou 2 dicionarios independentes, pois como eu fiz uma copia do 1 e quis modificar o nome
no 2, ficou diferentes esses dicionarios.

# Shallow Copy (Copia rasa)

PORÉM a partir do momento que eu tenho um dado MUTAVEL e faço um copy(), ele FAZ A COPIA DESSE DADO, mas ele 
vai apontar os 2 dicionarios para o mesmo dado na memoria, e vai acabar que esse dado vai ser igual nos 2 
dicionarios. Por isso é um Shallow Copy. Igual na OBS2 encima! 

EX: dicionario1 = {
        "nome": "Cleiton",
        "idade": 21,
        "dadoMutavel": ["cachorro", "papagaio", "periquito"]

}

dicionario2 = dicionario1.copy()
dicionario2["dadoMutavel"][0] = "gato"
print(dicionario1)
print(dicionario2)

# Deep Copy(Copia Profunda)

Agora para fazer uma copia profunda, tem que fazer o import do modulo copy, e usar o metodo .deepcopy(). 
Assim ele faz a copia dos dados de um para o outro, porem eles vao ser independentes um do outro.
Se usa com copy.deepcopy() e dentro desse parenteses poe o que voce vai copiar!

Ex: import copy

dicionario3 = {
    "comidas": ["Feijoada", "Macarronada", "Tacos"],
    "bebidas": ("Refrigerantes", "Sucos", "Bebidas Alcoolicas"),
    "preco": 20.99 , 16.00, 15.00
    }

dicionario4 = copy.deepcopy(dicionario3)
dicionario4["comidas"][2] = "Galinhada"

print(dicionario3)
print(dicionario4)

"""
import copy

#Shallow Copy
dicionario1 = {
        "nome": "Cleiton",
        "idade": 21,
        "dadoMutavel": ["cachorro", "papagaio", "periquito"]
}

dicionario2 = dicionario1.copy()

dicionario2["dadoMutavel"][0] = "gato"

dicionario2["nome"] = "João Paulo"

print(dicionario1)
print(dicionario2)

# Deep Copy
dicionario3 = {
    "comidas": ["Feijoada", "Macarronada", "Tacos"],
    "bebidas": ("Refrigerantes", "Sucos", "Bebidas Alcoolicas") ,
    "preco": (20.99 , 16.00 , 15.00)
}

dicionario4 = copy.deepcopy(dicionario3)
dicionario4["comidas"][2] = "Galinhada"

print(dicionario3)
print(dicionario4)