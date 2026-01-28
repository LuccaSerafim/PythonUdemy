"""
Aula comentando os possiveis problemas do nosso Exercicío Final e como resolver eles.

O 1° problema do codigo é como o cpf geralmente é mandando: "XXX.XXX.XXX-XX".
No meu codigo hoje esta assim: XXXXXXXXXXX.

Caso estivesse na escrita normal, poderiamos ter usado o metodo .replace(), onde temos que passar 2 coisas:
O que vamos substituir, e pelo oq substituir. Lembrando que funciona para strings e tambem podemos usar o replace
varias vezes na mesma linha.

Ex: cpf_para_verificacao = "746.824.890-70".replace(".", "") \
    .replace("-", "") \
    .replace(" ", "")

Um outro jeito é usando expressões regulares (Ele deu um exemplo apenas, vai ter uma sessão inteira so sobre isso)

Damos um: import re

cpf_para_verificacao = re.sub(
r"[^0-9]", # ele esta pegando tudo que não são numeros de 0 a 9(que é o que temos no nosso cpf)
"", # e substituindo por nada (pois queremos que nao seja nada)
"746.824.890-70"
)

Usando essa expressão é melhor pois podiamos ter um cpf assim: "746.sjkdnbsjdbsdkjf    jdfbndsjkfbsd   824.890-70"
E quando a gente desse o print, ia dar certo e tambem ia ser bom para usar com input do usuario.

Um segundo problema que nosso codigo tem é: Se por exemplo o nosso cpf for de numeros repetidos,
como: 11111111111, o codigo hoje vai aceitar. Porem a gente poderia fazer uma verificação se o que mandou é repetido
ou não.

Ex: repetido_ou_nao = entrada == entrada[0] * len(entrada)

Isso nos retorna um Bool( True ou False)
Na aula o professor mostrou outro import chamado sys, que tem uma função chamada sys.exit() que sai do codigo.

Essas soluções seriam boas, pois no nosso codigo do exercicio temos verificação de cpf valido ou nao, ai no caso de 
repetição ele daria invalido, se tivessimos um cpf cheio de coisas que nao seja numeros ele ia ficar bonitinho.

"""
import re 
import sys

cpf_para_verificacao = "746.824.890-70".replace(".", "") \
    .replace("-", "") \
    .replace(" ", "")
print(cpf_para_verificacao)


# cpf_para_verificacao = re.sub(
# r"[^0-9]", # ele esta pegando tudo que não são numeros de 0 a 9(que é o que temos no nosso cpf)
# "", # e substituindo por nada (pois queremos que nao seja nada)
# "746. ikehfeifhewikjfhwejkfhew wlkifdhewkifhw 824.890-70" 
# )

# print(cpf_para_verificacao)

# entrada = input("Digite algo: ")

# repetido_ou_nao = entrada == entrada[0] * len(entrada)

# if repetido_ou_nao:
#     print("É repetido!")
#     sys.exit()