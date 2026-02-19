"""
Esse exercicio 2 vão ser 3 funções:
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro.
"""

# Código mais simples e mais funcional:
def criando_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criando_multiplicador(2)
print(duplicar(2))

triplicar = criando_multiplicador(3)
print(triplicar(4))

quadruplicar = criando_multiplicador(4)
print(quadruplicar(3))


# Código simples
# def duplicar(numero):
#     return numero * 2 
 
# def triplica(numero):
#     return numero * 3

# def quadruplica(numero):
#     return numero * 4


# print(duplicar(2))
# print(triplica(3))
# print(quadruplica(4))



 

