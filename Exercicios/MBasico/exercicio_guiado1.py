"""
Exercicio guiado com while
Pro exercicio ele falou para botarmos um * de cada lado da letra de uma nome.
Ex: *A*
"""
# Meu código
nome = input("Digite seu nome: ")

tamanho_nome = len(nome)

contador = 0

while contador < tamanho_nome:
    if nome[contador] != " ":
        print("*" + nome[contador] + "*", end=" ")

    else:
        print(" ", end=" ")
    
    contador +=1
    
# Código do professor, que percebi que é mais simples tbm
# nome = 'Maria Helena'  # Iteráveis

# indice = 0
# novo_nome = ''
# while indice < len(nome):
#     letra = nome[indice]
#     novo_nome += f'*{letra}'
#     indice += 1

# novo_nome += '*'
# print(novo_nome)
   