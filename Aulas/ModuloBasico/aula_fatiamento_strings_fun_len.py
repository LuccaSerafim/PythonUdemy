"""
Aula de fatiamento de strings e a função len
No fatiamento o nome ja diz, voce pode pegar o inicio, o fim ou um passo [i:, f:, p:] 
OBS: to dando essas virgulas so para separar mesmo
A função passo nos diz de quantos em quantos caracteres ele vai pular, geralmente de 1 em 1.
Podemos usar o passo tambem com os numeros invertidos, onde tem a opção dele inverter nossa string
Vamos supor que voce tenha uma string de nome, e quero pegar uma fatia que vai de um determinavel pedaço
e acabe em outro.
Lembrar que indices começa no 0
Ex: nome = "João da Silva" #tem 12 indices(0 a 11 positivos), os negativo são inversos,
nesse exemplo(-12 a -1), sendo o -12 o primeiro indice, nesse caso o J.
E quero pegar do indice 3 ate o 7. print(nome[3:8]) 
OBS: fui ate o 8 pois assim ele acaba certinho no 7, caso queria que vai ate o final da string, basta omitir ela
ex: print(nome[3:])
Podemos omitir o começo tbm caso queiramos que vai do começo.

Já a função len retorna a quantidade de caracteres da string.
Lembrar que indices é diferente de caracteres.
A função len tbm tem outras funções, so que por enquanto vamos ver essa.

"""

nome = "João da Silva"
print(nome[3:8])
print(nome[3:])
print(nome[:8])
print(nome[3:8:1])
print(len(nome[::-1]))


