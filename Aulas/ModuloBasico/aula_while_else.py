"""
Aula falando sobre while else
O while else não é muito utilizado mas é uma opção.

O else so vai ser executado quando o while for parado de executar sem ser forçado(break)
Caso tenha um break dentro do while o else não vai ser executado
"""


frase = input("Digite um frase: ")

i = 0

while i < len(frase):

    letra = frase[i]

    
    if " " in letra:
        break

    print(letra)
    i += 1

else:
    print("Acabou o while")

print("Se chegou aqui o else nem rodou.")