"""
Exercício 3: Sistemas de perguntas e respostas (Dict)
"""
# Meu código:
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
     
     while True:

        for chave, valor in pergunta.items():
            if chave != "Opções" and chave != "Resposta":
                print(f"{chave}: {valor} ")
        
            
        for indice, opcao in enumerate(pergunta.get("Opções")):
            print(f"{indice}) {opcao}")

        escolha = input("\nEscolha uma opção: ")

        resposta_usuario = pergunta["Opções"][int(escolha)]  
        respostacorreta = pergunta.get('Resposta')

        if resposta_usuario == respostacorreta:
            print(f"Resposta: {respostacorreta}", "\nVocê Acertou!")
            break

        else:
            print("Você errou, tente novamente")
            continue

# Exercicio que mexeu bastante com o get e items dos dicionarios, fiquei um pouco em duvida de como que faria para
# imprimir tanto a chave e o valor nas perguntas, quanto os indices nas opções.
# Melhorar isso!!!!!!    

# Código do professor abaixo:

# qtd_acertos = 0
# for pergunta in perguntas:
#     print('Pergunta:', pergunta['Pergunta'])
#     print()

#     opcoes = pergunta['Opções']
#     for i, opcao in enumerate(opcoes):
#         print(f'{i})', opcao)
#     print()

#     escolha = input('Escolha uma opção: ')

#     acertou = False
#     escolha_int = None
#     qtd_opcoes = len(opcoes)

#     if escolha.isdigit():
#         escolha_int = int(escolha)

#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < qtd_opcoes:
#             if opcoes[escolha_int] == pergunta['Resposta']:
#                 acertou = True

#     print()
#     if acertou:
#         qtd_acertos += 1
#         print('Acertou 👍')
#     else:
#         print('Errou ❌')

#     print()


# print('Você acertou', qtd_acertos)
# print('de', len(perguntas), 'perguntas.')
