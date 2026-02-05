"""
Aula falando de argumentos nomeados e não nomeados em funções.

Os argumentos nomeados tem nome com sinal de igual, já os não nomeados recebem apenas o argumento(valor).
Os não nomeados também são chamados de posicionais.

Os nomeados a gente chama direto na execução da função.
Ex: def conta(x, y):
    conta = x * y
    print(f"A conta entre {x} e {y} é = {conta}")


conta(10, 45) # assim é nao nomeado

Suponha que eu quero que o y fosse o 10 e o 45 o x, porem sem inverter eles, eu posso so fazer assim:
conta(y= 10, x= 45) # assim e nomeado

OBS: Não é interessante misturar o nomeado com o nao nomeado, pois depois que voce nomeou um argumento
mas nao nomeou os outros que vem depois vai dar erro.

Ex: conta(y= 55, x) # vai dar erro pois voce nao nomeou o outro argumento depois de ter nomeado um.

"""

def conta(x, y, z):
    conta = x * y + z
    print(f"Essa conta entre {x} , {y} e {z} é = {conta}")


conta(10, 45, 22)
conta(y= 10, z= 45, x = 22)