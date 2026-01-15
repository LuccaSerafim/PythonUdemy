"""
Aula introdutoria de For(outro laço de repetição)
For mais usado para iterar coisas, onde passamos uma variavel onde ele vai iterar cada elemento para a variavel
que eu criei. OBS: no caso do for não pegamos o indice em si e sim o valor.
Ex: for valor in nome:
        print(letra)

Não e comum usar o while com coisas que a gente sabe onde termina, exemplo: tamanho em indice de uma string.
O comum de usar o while é quando a gente não sabe onde termina, por exemplo com um input do usuario
para verificar uma senha, ai nesse caso podemos usar direto o while True.


"""
# Mesmo exemplo de codigo de botar o * antes e depois no nome
# Com o for foi mais simples.
nome = "Cleiton"
novo_nome = ""

for letra in nome:
    novo_nome += f"*{letra}"
    print(letra)

print(novo_nome + "*")