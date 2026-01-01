"""
Aula de formatação de strings voltada mais a f-strings
Temos basicamente os mesmos "alfabetos" da interpolação, porem com alguns diferentoes
s = string
d  = números inteiros
f = float
x e X = hexadecimal (ABCDEF0123456789)
Sinal  dos caracteres(><^)(quantidade)
> = esquerda
< = direita
^ = centro
= Força o numero a aprecer antes
Podemos usar esses caracteres caso, por exemplo, preencher um espaço de uma string qualquer a esquerda dele
10 vezes. Ex: print(f"{qualquer: >10}"). Tambem podemos botar qualquer caracter para preencher junto.
Exemplo: print(f"{qualquer: #>10}")
Podemos usar tambem 
sinais = + ou -
Lembrar que pra usar qualquer um desse "alfabetos", botar o : antes de usar eles



"""
risada =  20 * "K"
print(f"{risada:o>40}")
print(f"{risada:o<40}")
print(f"{risada:o^40}")



