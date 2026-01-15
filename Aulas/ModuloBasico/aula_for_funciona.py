"""
Aula é entendendo como que o for funciona de fato(por baixo dos panos do for).
Porém nao precisa saber como ele funciona para usar ele, uma analogia da aula foi que não precisamos entender,
como o carro funciona para dirigir, temos apenas que saber dirigir.

Iteravel = str, range, etc(__iter__)
Iterador = quem sabe entregar um valor por vez. (como se fosse um entregador).
Next = me entrega o proximo valor que tiver disponivel dentro do iter.
Iter = me entrega o objeto que sabe iterar minha string por exemplo.

Tanto o next quanto o iter tem a propria funçao no python: iter() , next()
"""

# Por baixo dos panos o for funciona assim:
# nome = input("Digite seu primeiro nome: ") # iteravel
# iterador = iter(nome) # iterador

# while True:

#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

# o For funciona desse jeito abaixo . Ele acaba fazendo esse "Tratamento" para não estourar excessão 
nome = input("Digite seu primeiro nome: ") #iteravel
iterador = iter(nome) #iterador

for letra in nome:

    letra = next(iterador)
    print(letra)
    
   