"""
Aula falando sobre valores padrão para parametros das funções.

E comum a gente definir uma função, e num determinado parametro a gente definir um não valor para ele.

Toda vez que a gente definir um valor padrao para um parametro, todos os outros parametros apos precisam de um
valor padrao. 

Definir um valor padrao para um parametro é equivalente a pegar uma variavel e definir ela.

Parte do codigo da aula:
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.

"""

# Código do professor, fiquei sem criatividade

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)