"""
Aula sobre Operação Ternária (condicional de uma linha) # Basicamente um if else de uma linha

Estrutura: <valor> if <condição> else <outro valor>

Temos o tal valor, que vai ver a condição dele, se for verdadeira esse valor sera retornado, se for falso
o outro valor vai ser retornado.

Ex: condicao = 10 == 10
aula = "certo" if condicao else "falso"
print(aula)

Isso verifica se 10 é igual a 10, se for vai imprimir "certo" e se não for vai imprimir "falso".
Como sabemos que é igual nos tras : "certo"

Podemos fazer varias operações dentro de uma (Não recomendado fazer).
EX: print("Oi" if True else "Não oi!" if False else "acabou")

"""
condicao = 10 == 11
aula = "certo" if condicao else "falso"
print(aula)

# print("Oi" if False else "Não oi!" if False else "acabou") #Não é recomendado fazer
