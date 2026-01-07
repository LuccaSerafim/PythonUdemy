"""
Meio que uma continuação da aula do while apresentando tambem a função continue
Diferentemente do break, o continue ele volta pro começo do laço e roda novamente
(Caso a condição for verdadeira ne)
Lembrando que tanto o break como o continue vão ser executadas no while mais proximas delas, pois podemos ter 
while dentro de while.


"""
# Código do professor.
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break


print('Acabou')