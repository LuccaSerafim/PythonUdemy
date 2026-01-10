
# A aula vai ser sobre verificar qual letra aparece mais vezes em uma determinada frase.
# Lembrando que \ quebra a linha, usar fora das "" e depois usar "" caso queira escrever mais alguma coisa.
# Dentro do print não precisa usar a \ para quebrar a linha.
# Temos a função .count() que nos mostra já quantas vezes tal string apareceu no que queremos descobrir.
# OBS: funciona apenas com string essa função.
# No exemplo que ele fez, ele tinha uma frase pronta, pegou cada indice dela dentro do while ja,
# e depois usou o .count(). No print vai aparecer a frase e ao lado de cada letra o número de quantidade de vezes
# que a letra apareceu.


frase = input("Digite uma frase: ")

i = 0
qtd_apareceu_mais = 0
letra_apareceu_mais = ""

while i < len(frase):
    letra_atual = frase[i]

    if " " in letra_atual:
        i += 1
        continue

    qtd_apareceu_mais_atual = frase.count(letra_atual)

    if qtd_apareceu_mais < qtd_apareceu_mais_atual:
        qtd_apareceu_mais = qtd_apareceu_mais_atual
        letra_apareceu_mais = letra_atual


    i += 1

print(
    "A letra que apareceu mais vezes foi "
    f"'{letra_apareceu_mais}' que apareceu "
    f"{qtd_apareceu_mais}x"
)