"""
Aula mostrando sobre o comando Format. Outra forma de formatar strings
Usa-se o .format() e dentro dessa chaves que botamos os argumentos. 
Na hora do print, ele vai ver as {} e vai pegar o primeiro argumento que ta dentro do .format 
e caso temos mais chaves ele vai seguir na ordem, se tivermos 3 chaves, ele vai ver os argumentos dentro do .format
e vai seguir a ordem. ex: .format(a, b, c).
Da para botar o :.2f dentro das chaves tbm, caso queremos que algum numero por exemplo mostre suas 2 casas decimais.
Se botassemos uma 4° {} vai aparecer o erro de estar buscando algo que acabou. mas se no format a gente botar 
mais um argumento vai imprimir o que botamos, mas se a gente so botar a {} sem um outro argumenti vai dar erro
Podemos trabalhar com indices tbm, ai nao precisamos mais confiar nas {} vazias. podemos multiplicar botando
o numero dos indices dentro das chaves. Lembrando que os indices começam no 0. Caso usar os numeros, botar numero
em todas as {} senao da erro.
Podemos nomear parametros tbm. OBS: Caso comecamos no argumento 1 temos que nomear todos que vem depois dele tbm
 Exemplo: exemplo.format(
         a, b, nome3=c
).
Caso nomeamos o parametros temos que fazer a chamada dele nas {}. Exemplo: c = {nome3:.2f} 
"""


a = "Oi!"
b = 'tchau'
c = 3.4

exemplo = 'a = {0} b = {1} b = {nome3}  c = {nome3:.2f} '
formato = exemplo.format(a, b, nome3 = c)

print(formato)