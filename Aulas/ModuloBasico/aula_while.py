"""
Aula sobre repetição (while) 
While = enquanto
O while executa um bloco de código enquanto a condição for verdadeira, parecido com um if.
Tomar cuidado ao fazer um codigo com while para nao cair em um loop infinito
Caso não temos uma ação para parar o while de rodar, podemos usar o break; para 'quebrar' o laço mais proximo dele,
no nosso caso o while

Todos os operadores aritméticos podem ser combinandos com os operadores de atribuição
= ; += ; -= ; *= ; /= ; //= ; **= ; %=

Funciona com strings tambem, se quisermos concatenar ou repetir algo.



"""
# Verificação letras alfabeto
letra_secreta = "X"
tentativas = 5
acertou = False

print("Tente adivinhar minha letra secreta!")

while tentativas > 0 and not acertou:
    palpite = input(f" Você tem {tentativas} tentativas. Digite uma letra do alfabeto: ")

    if  palpite == letra_secreta:
        print("Você acertou a letra secreta!!!!")
        acertou = True

    else: 
        print("Você errou!")
        tentativas -= 1

    
    
if not acertou:
     print(f"A letra era {letra_secreta}")


   

    
    