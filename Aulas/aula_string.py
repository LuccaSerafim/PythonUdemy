"""
Strings sao dentros dentro de aspas
podem ser aspas simples ou aspas duplas
Caso eu queira fazer um escape, uso a \ para pular o caracter
Caso queira mostrar o caracter de escape usa o r antes das aspas
geralmente nao se usa o r nem o escape, o r é usado mais em expressoes regulares
Exemplo (r"Eu gosto de \"Basquete\"")
Caso queira botar uma string com essa marcaçao de aspas, pode usar as simples dentro de uma dupla e vice versa
Exemplo ('Eu gosto de "Basquete"') ou ("Eu gosto de 'Basquete'")
"""

print('Oi!')
print("Oi!")
print(("Eu gosto de \"Basquete\""))
print(r"Eu gosto de \"Basquete\"")
print('Eu gosto de "Basquete"')
print("Eu gosto de 'Basquete'")

