"""
Aula mostrando métodos úteis para strings (Pode ser que acaba envolvendo as lists tbm)

Eles são: split, join

split = divide uma string
join = une uma string
strip = corta os espaços do começo e do fim

Suponha que eu tenha uma frase qualquer e eu quero quebrar ela nos espaços em brancos.
Ex: frase = "Uma frase qualquer da aula" | lista = frase.split()

OBS: Geralmente passa um argumento dentro desses (), porem se nao botar nada ele ja divide pelos espaços em brancos.

Podemos separar a frase usando o for tbm.
Assim: for i, frase2 in enumerate(lista2):
            print(lista2[i])


O strip ele tem 3 jeitos: split() | lstrip() | rstrip()
O 1° ele tira direto os espaços dos 2 lados
O 2° tira apenas o da esquerda e o 3° apenas da direita

É importante lembrar que possa ser que a gente queria um valor antigo (mutavel) em algum momento do codigo, por isso
é interessante não modificar algo direto mutavel

Ja o join a gente começa com uma string ("") junto com o metodo .join(), nesses () do join passamos algo
iteravel. Nessa string a gente pode botar qualquer coisa, pois na hora que der o join o que passamos na string
vai juntar com o interavel 

Ex: uniao = "-".join(listanormal)


"""

frase = "Uma frase qualquer da aula" 
frase2 = "         Olha só, um avião no céu         "
lista = frase.split() # ja separa pelos espaços em branco
lista2_crua = frase2.split(",") # Aqui to separando direto pela ,

listanormal = []

for i, frase2 in enumerate(lista2_crua):

    listanormal.append(lista2_crua[i].strip())
   

# print(listanormal)
# print(lista2_crua)

uniao = "-".join(listanormal)
print(uniao)