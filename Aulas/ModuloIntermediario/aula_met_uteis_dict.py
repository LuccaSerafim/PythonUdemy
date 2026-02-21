"""
Aula sobre metodos uteis dos Dicionarios (Dicts)

OBS: Essa aula foi dividida em 2 no curso: Aulas 123 e 125!

OBS2: Se temos varias chaves iguais, mas com valores diferentes, apenas o ultimo vai ser usado. 
Como se a gente criasse uma chave e atualizasse ela varias vezes.

Métodos Mais Utilizados:

len = retorna a quantidade de chaves que tem no dicionario; len()

keys = retorna as chaves que temos. Se usa com .keys(). É um iteravel tbm.

values = retorna os valores que temos. Parecido com o keys. Se usa com .values() e tbm é iteravel.

items = retorna a chave e o valor (cada um correspondente). Se usa com .items(). Pode ser usado parecido com o 
enumerate.

setdefault = adiciona um valor se a chave não existe. Tem que passar 2 parametros (O nome da chave e o valor).
Se usa com .setdefault() . OBS: Se a chave ja existe o set default não faz nada!!!

get = obtem uma chave. Visto na aula de manipulaçao de chave e valor. Se usa com .get() onde passamos o nome da
chave e um valor padrao nesses (). Caso tenha a chave passada ele retorna o valor dessa chave, se nao tiver a chave,
por padrao ele volta None mas podemos passar um valor padrao nos () para retornar!

pop = apaga um item com a chave especifica (tipo del, porem um pouco diferente). Nos dicionarios o pop voce tem que
ESPECIFICAR A CHAVE QUE QUER REMOVER, ai ele retorna o valor dessa chave e apaga do dicionario. Se usa com .pop(),
nesses () poe a chave que quer remover.

popitem = remove a ultima chave do seu dicionario. Se usa com .popitem(). E igual o pop ele retorna a chave e o valor
antes de remover

update = atualiza um dicionario com outro. Temos algumas formas de usar o update.
o 1°: d1.update({
        "nome": "novo nome",
        }). 
Usando o update assim voce pode atualizar chaves existentes que ele nao interfere nas outras chaves e tambem pode
adicionar outras chaves tbm.

o 2°: d1.update(nome="novo nome", chavenova= "chave criada"). 
Podemos escrever assim tambem que dependendo da sua atualização fique ate mais facil assim!.

Sempre temos que passar algo nos parenteses do .update(), podendo passar iteraveis.
Porem com os iteraveis como tuplas e listas ja tem que criar antes passando chave e valor.
Ex: lista = [["idade", 20], ["sobrenome", "Junior"]]
tupla = ("altura", 1.90) , ("País", "Japão")

d1.update(lista) ou d1.update(tupla)
print(d1)

"""

familia = {
    "pessoas": ["José", "João", "Thaynna", "Cleiton"],
    "idades": [59, 23, 21, 44],
    "alturas": [1.80, 1.73, 1.65, 1.83],
    "Hobbys": ["Música", "Skate", "Pintar", "Jogo online"]
}

pets = familia.setdefault("Pets", ["Cachorros"])
print(len(familia))
print(list(familia.keys()))
print(list(familia.values()))

for chave, valor in familia.items():
    print(chave, valor)

print(familia.get("Endereço", "Não tem!"))

remover = familia.pop("alturas")
print(remover)

ultimachave = familia.popitem()
print(ultimachave)

print(familia)

