# Id = Identidade
# Podemos usar o id para verificar a identidade das coisas com a função id()
# Ao usar o id() verificamos a identidade do elemento na memoria
# Dependendo de algumas coisas, pode ser que o id de 2 variaveis diferentes mas que tem o mesmo valor pode retornar o mesmo id

# Exemplo com mesmo valor de id
nome1 = "João"
nome2 = "João"
print(id(nome1))
print(id(nome2))

# exemplo com valores diferentes
sobrenome1 = "Henrique"
sobrenome2= "Pedro"
print(id(sobrenome1))
print(id(sobrenome2))