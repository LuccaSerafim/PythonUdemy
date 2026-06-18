"""
Aula mostrando os operadores úteis do set:

1) União (union): Usa o caracter "|" para fazer a união entre os sets

2) Interseção: Usa o caracter "&" e mostra os itens presentes em ambos

3) Diferença: Usa o caracter "-" e mostra os presentes apenas no set da esquerda

4) Diferença Simétrica: Usa o caracter "^" e mostra os itens que não estão em ambos os sets




 
"""

# Exemplo union

set1 = {1,2,4}
set2 = {3,5,6}

union = set1 | set2
# print(union)

# Exemplo interseção
set3 = {1,2,4}
set4 = {2,4,6}

intersec = set3 & set3
# print(intersec)

# Exemplo diferença. OBS: NA HORA DE FAZER A DIFERENÇA VAI OCORRER DIFERENÇA DE RESULTADO DEPENDENDO DO SET MAIS A ESQUERDA

set5 = {5,6,7}
set6 = {6,7,8}

dif = set5 - set6
dif2 = set6 - set5

# print(dif, dif2)

# Exemplo diferença simetrica

set7 = {8,9,10}
set8 = {9,10,11}

dif_simetrica = set7 ^ set8
print(dif_simetrica)