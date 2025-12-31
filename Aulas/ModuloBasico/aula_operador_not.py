# Usado para inverter expressoes
# usado mais para checar coisas.Ex: se a senha nao for tal ...
# not True = False
# not False = true

nome = input("Digite seu 1° nome: ")

if not nome == "Enzo":
    print(f'Seu nome não é enzo e sim {nome}')

else:
    print(f"Seu nome é {nome}")


print(not 0.0)