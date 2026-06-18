"""
Aula mostrando alguns métodos uteis para o set.

Métodos:
add = Se usa com .add(), onde tem que passar apenas um argumento nos () pois pode dar erro se passar mais de 1.

update = Se usa com .update() e é parecido com o add, porem com o update se vc passar o argumento ele vai iterar ja,
no caso podemos passar um iteravel dentro do update e adicionar mais de 1 argumento, por exemplo a tupla.

clear = Se usa com .clear() e ele limpa o set mesmo.

discard = Se usa com o .discard() e ele remove um valor do set, e por não aceitar indice no set tem que passar
o valor que quer apagar.
"""

vazio = set()
vazio.add(1)
vazio.add("Olá")
vazio.update("iterou a frase completa")
vazio.update(("Testando o update botando mais de 1 argumento", 20, 10))
vazio.discard("iterou a frase completa")
vazio.discard(20)
print(vazio)