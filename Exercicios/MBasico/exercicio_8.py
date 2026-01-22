"""
Exercício 8: Criar uma lista de compras com Listas.

Instruções abaixo:
O usuario deve ter a possibilidade de inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com erros de indices inexistentes.

"""

lista = []

while True:
    
    opcao = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar [s]air: ")

    if opcao.startswith("i"):
        produto = input("Produto: ")

        if not produto:
            print("Você não adicionou nada.")
            continue
        
        lista.append(produto)
        print("Produto adicionado")

    elif opcao.startswith("a"):
        apagar = input("Escolha o indice que deseja apagar: ")

        if not apagar.isdigit():
            print("Voce nao digitou um indice")
            continue

        remover = int(apagar)

        if remover not in range(len(lista)):
            print("Não é possivel apagar esse indice!")
            continue

        lista.pop(remover)
        print("Item removido")

    elif opcao.startswith("l"):

        if lista:
            for indice, produto in enumerate(lista):
                print(indice, produto)
                
        else:
            print("Sua lista está vazia")

    elif opcao.startswith("s"):
        print("Você escolheu sair!")
        break
    
    else:
        print("Você não escolheu uma opção válida, por favor selecione uma.")
        

# Apos fazer esse codigo so tenho que relembrar do not, e de que o pop nesse codigo apaga apenas o selecionado e reorganiza.
# Lembrar que o isdigit() ve se o que foi digitado e um caracter numerico, perfeito para ver se sao indices.




        
        

