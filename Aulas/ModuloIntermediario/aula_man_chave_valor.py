"""
Aula (Básicão) de manipulação de chave e valor (Dict)

Podemos criar uma chave com um sinal de atribuição, suponha que eu tenho um dicionario e eu por algum motivo
queira adicionar uma nova chave(lembrar com indice), ai eu faço assim:

dicionario = {}

dicionario["estado civil"] = "Casado"

print(dicionario). 

Com esse formato eu acabo de adicionar uma nova chave, com um valor aleatorio. 

Porém poderiamos ter feito dinamicamente assim:

chave = 'idade'
dicionario[chave] = 25

Podemos usar o metodo del para apagar uma chave. Assim como o CRUD(Create, Read, Update, Delete)!!!!!!


Temos um outro metodo que chama .get() usado para tentar obter uma chave, ele retorna None se a chave não existir,
e se existir, ele retorna o valor dessa chave.

Ex: print(dicionario.get("cidade", None)) 
OBS: Esse none que eu escrevi ao lado de cidade é um valor padrao, que vc pode botar qualquer coisa, mas como
é mais esse get é mais usado para fazer um condicional é recomendado deixar como None.

Geralmente é usado com if e faz a verificação com is none, ex:

if dicionario.get("cidade") is None:
    print("Não existe esse chave")

else:
    print("Existe essa chave")

"""

dicionario = {}

dicionario["estado civil"] = "Casado"

chave = 'idade'
dicionario[chave] = 25

print(dicionario)

if dicionario.get("cidade") is None:
    print("Não existe esse chave")

else:
    print("Existe essa chave")

# print(dicionario.get("cidade", None))
