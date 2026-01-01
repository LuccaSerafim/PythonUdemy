"""
Nesse exercicios vamos fazer basicamente tudo do mais importante que ja vimos ate agora.
O exercicio em si pede:
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."

    Ao fazer esse exercicio percebi que tenho que rever aula como in e not.
    Da pra fazer a função len dentro da f-string, bastava {len(nome)}
"""
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
letras = len(nome)


if (nome and idade):
    print(f"Seu nome é {nome},")
    print(f"Seu nome invertido é {nome[::-1]},")

    if " " in nome:
        print("Seu nome contem espaços")
    else:
        print("Seu nome não tem espaços")
        
if (nome and idade):
            print(f"Seu nome tem {letras} letras, ")
            print(f"A primeira letra do seu nome: {nome[0]}")
            print(f"A ultima letra do seu nome: {nome[-1]}")

elif (not nome == " " or idade == " " ):
            print("Desculpe, você deixou campos vazios.")



