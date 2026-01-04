"""
Exercício1:
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Exercício2:
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Exercício3:
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# Exercício1:
numero = input("Digite um número: ")

try:
    numero_float = float(numero)

    if numero_float == int(numero_float):
        numero_int = int(numero_float)

        if (numero_int % 2 == 0):
            print("Este é um número par")

        else:
            print("Este é um número impar")

    else:
        print("Este não e um número inteiro")

except:
    print("Voce nao digitou um numero valido")

# Rever try e except pois tive problemas, Ou ter usado if else com isdigit.

# Exercicio2:
hora = int(input("Digite que horas são: "))
DIA = (0 <= hora <= 11)
TARDE = (12 <= hora <= 17)
NOITE = (18<= hora <= 23)

if DIA:
    print("Bom dia!")

elif TARDE:
    print("Boa tarde!")

elif NOITE:
    print("Boa noite!")

# Relembrar tambem dos operadores <, >. Mas consegui mais de boas

# Exericio3:
nome = input("Digite seu primeiro nome: ")
NOME_CURTO = 0 <= len(nome) <=4
NOME_NORMAL = 5 <= len(nome) <= 6
NOME_GRANDE = len(nome) > 6

if NOME_CURTO:
    print("Seu nome é curto")

elif NOME_NORMAL:
    print("Seu nome é normal")

elif NOME_GRANDE:
    print("Seu nome é grande")

# Consegui mais tranquilo, so revi a estrutura do len mesmo no exercicio 4.
