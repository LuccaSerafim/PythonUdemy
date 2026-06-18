"""
Aula introdutória a estrutura de dados do tipo SET
Set são conjuntos iguais os da matemática

Set é um tipo MUTAVEL, porem que só aceita tipos IMUTAVEIS dentro dele.

Para criar um set, podemos usar o método set() ou usando as {}. Porém diferentemente dos dicts, as chaves no set
só recebem valor.

OBS1: podemos ter um set vazio, assim: set(). Porém se usarmos as {} vazia assim, ele é um dicionario e nao um set.
Tem que passar os valores se for usar as {}

Pelo set receber iteraveis nele, ele vai iterar um por um, por exemplo se eu fizer um:
teste = set("Celbit")
print(teste). Ele vai iterar a palavra "celbit" letra por letra.

OBS2: pode ocorrer de na hora de iterar, ele nao seguir a ordem.

O set é eficiente para remover valores duplicados de iteraveis.

ex: repetido = (1,1,1,1,3,3,4,5,6,6,6,7)
tirando_repeticao = set(repetido)
print(tirando_repeticao)

O set não aceita tipos MUTAVEIS dentro dele, da erro caso ocorra.

O set também não tem indices, então eu não posso fazer um print(tirando_repeticao[2]) pois vai dar erro.

Podemos fazer iterações sobre o set, como: for, in, not in
"""

teste = set("Olá Mundo")
print(teste)
repetido = (1,1,1,1,3,3,4,5,6,6,6,7)
tirando_repeticao = set(repetido)
print(tirando_repeticao)