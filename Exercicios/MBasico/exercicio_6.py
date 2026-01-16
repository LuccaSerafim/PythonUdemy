"""
Exercício 6 - Palavra secreta. Instruções abaixo:

Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
# Meu código:

palavra_secreta = "cachorro"
tentativas = 0
letras_acertadas = []

while True:
    descobrir_palavra = input("Digite uma letra: ")
    
    if not descobrir_palavra:
        print("Você não digitou nada, por favor digite uma letra")
        continue

    if len(descobrir_palavra) > 1:
        print("Digite apenas uma letra")
        continue
    
    tentativas +=1

    if descobrir_palavra in palavra_secreta:
        letras_acertadas += descobrir_palavra

    palavra_formada = ''
    
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    
    print(palavra_formada)
    
    if palavra_formada == palavra_secreta:
        print("Você acertou a palavra secreta!!!!!\n" 
              f"A palavra era: {palavra_secreta}\n"
            f"{tentativas} Tentativas"
              )
        break

# Ao realizar esse codigo percebi que tenho que pegar mais pratica em pensar na hora de botar o * na palavra
# Tambem em pegar mais a manha do for, lembrar também do not. Do \n para quebrar as linhas.

# Código do professor abaixo:
# import os

# palavra_secreta = 'perfume'
# letras_acertadas = ''
# numero_tentativas = 0

# while True:
#     letra_digitada = input('Digite uma letra: ')
#     numero_tentativas += 1

#     if len(letra_digitada) > 1:
#         print('Digite apenas uma letra.')
#         continue

#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada

#     palavra_formada = ''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += '*'

#     print('Palavra formada:', palavra_formada)

#     if palavra_formada == palavra_secreta:
#         os.system('clear')
#         print('VOCÊ GANHOU!! PARABÉNS!')
#         print('A palavra era', palavra_secreta)
#         print('Tentativas:', numero_tentativas)
#         letras_acertadas = ''
#         numero_tentativas = 0

# Ao ver o codigo do professor percebi que ele fez basicamente o mesmo que eu, então gostei de como ficou



