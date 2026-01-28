"""
Aula de desempacotamento de chamadas: Métodos e Funções.

Temos 2 jeitos de desempacotar: Fazendo direto no for e fazendo direto no print.

EXFOR: lista = ["João", "Thaynna", 1, 2, "Oi!"]
    for texto in lista:
        print(texto, end=' ')
Isso nos tras os valores da lista um ao lado do outro.

EXPRINT: print(*lista).
Isso ja nos tras os valores um do lado do outro, bem mais rapido do que o for.

Funciona com qualquer ITERAVEL

O professor mostrou usando o exemplo da outra aula, das listas da salas:

salas = [
    ["Maria", "Helena"] , # 0 (indice da sala) , dentro desse indice tenho mais 2 indices(0,1)
    ["Eliane",] , # 1 (indice da sala) , dentro desse indice tenho mais 1 indice (0)
    ["Luiz", "João", "Eduarda"] # 2 (indice da sala) , dentro desse indice tenho mais 3 indices (0,1,2)
    
    
    
    # ["Luiz", "João", "Eduarda", (0, 10, 20, 30)] # 2 (indice da sala) , dentro desse indice tenho mais 4 indices(0, 1, 2, 3)   
]

Fazendo o print(*salas) ja tiramos aqueles primeiros []. Ficando agora assim: 
['Maria', 'Helena'] ['Eliane'] ['Luiz', 'João', 'Eduarda']

Porem podemos deixar cada sala um embaixo do outro usando o sep="\n"

Ficando mais legivel:

['Maria', 'Helena']
['Eliane']
['Luiz', 'João', 'Eduarda']

"""

string = "Testando, a, chamada, de, função"

lista = ["João", "Thaynna", 1, 2, "Oi!"]

salas = [
    ["Maria", "Helena"] ,
    ["Eliane",] , 
    ["Luiz", "João", "Eduarda"] 

]

# for texto in lista:
#     print(texto, end=' ')


print(*salas, sep="\n")
print(*lista)
print(*string)