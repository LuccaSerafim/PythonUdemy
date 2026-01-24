"""
Aula de iteralvel dentro de iteravel.


Exemplo da aula Listas dentro de Listas. No exemplo que ele fez na aula foi uma lista que representa sala,
e dentro dessa lista sala ele fez 3 listas com alunos dentro.
Mais ou menos assim: 
salas = [
    ["Maria", "Helena"] ,
    ["Eliane",] ,
    ["Luiz", "João", "Eduarda"]        

]

Se eu fizer print(salas[2]) eu vou receber essa lista : ["Luiz", "João", "Eduarda"], mas agora se eu fizer
print(salas[2][1]) eu vou entrar primeiro no indice 2 da salas e achar o valor que corresponde ao indice 1, nesse
caso é o João


Para complicar mais um pouquinho o professor adicionou uma tupla no indice 2 de salas, ficando assim:
["Luiz", "João", "Eduarda", (0, 10, 20, 30)] e pediu para buscarmos o valor 20.
Acredito que fica assim: print(salas[2][3][2])

Ao inves de ficarmos fazendo prints para acessar cada coisa, é mais facil fazermos for.

"""

salas = [
    ["Maria", "Helena"] , # 0 (indice da sala) , dentro desse indice tenho mais 2 indices(0,1)
    ["Eliane",] , # 1 (indice da sala) , dentro desse indice tenho mais 1 indice (0)
    ["Luiz", "João", "Eduarda"] # 2 (indice da sala) , dentro desse indice tenho mais 3 indices (0,1,2)
    
    
    
    # ["Luiz", "João", "Eduarda", (0, 10, 20, 30)] # 2 (indice da sala) , dentro desse indice tenho mais 4 indices(0, 1, 2, 3)   
]

# print(salas[2])
# print(salas[2][1])
# print(salas[2][3][2])

for turmas in salas:
    print(f"As turmas são: {turmas}")

    for alunos in turmas:
        print(f"Os alunos de cada turma são: {alunos}")

        

