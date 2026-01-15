"""
Essa aula é mais para mostrar que coisas do while funcionam com o for também.
Como: break, continue, if, else, etc.

Lembrando que geralmente usamos o for quando conhecemos o inicio, meio e fim de algo. 
No caso acaba sendo uma repetição onde temos uma noção da onde vai terminar. Ao contrario do while.

Geralmente na programação ao usar números definimos as variaveis: i, j, k, etc.
O continue e o break funcionam da mesma forma do while com o for, no caso o continue voltando para o começo do laço
e iniciando novamente e o break terminando o laço. Ambos para o for mais proximo.

"""
# Código do professor, não pensei em nada mas achei interessante
# Nesse caso o i seria como uma linha e o j como uma coluna

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')