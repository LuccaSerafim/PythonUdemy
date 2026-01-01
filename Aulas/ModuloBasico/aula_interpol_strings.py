"""
Aula de interpolação basica de string(%)
A interpolação tbm é um tipo de formatação no python
A interpolação e basicamente a mesma coisa que fizemos com o format,
mas de um jeito diferente.
O "alfabeto" basico da interpolação é:
s = string
d ou i = números inteiros
e = notação cientifica
f = float
x e X = hexadecimal (ABCDEF0123456789). OBS: x(minusculo) gera um hexadecimal minusculo. X(maiusculo) gera um maisculo.
Caso a gente gere um hexadecimal que deu apenas uma casa, podemos preencher o resto com %04X.(preencher com 0 e mostrar as 4 casas.)
Jeito de usar é % e o tipo(o alfabetozinho). Apos isso botar um % na frente da string e caso temos mais de uma
informação na interpolação botar um () com as variaveis dentro.
Ex: variavel = "%s, o total das compras foram %f" % (nome, total)
print(variavel).
Caso queremos definir a quantidade de casas decimais igual na f strings, fazemos assim: "%.2f"


"""

nome = input("Digite seu nome: ")
mercado = input("Digite um item de mercado: ")
preco = float(input("Digite o preço do produto que você escolheu : R$ "))

print(
    "Seu nome é %s, o item escolhido foi %s e ele custa R$%.2f" % (nome, mercado, preco)
)
