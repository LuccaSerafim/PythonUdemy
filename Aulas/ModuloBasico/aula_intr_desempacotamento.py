"""
Aula introdutoria de desempacotamento e empacotamento

Todo tipo iteravel a gente pode desempacotar. 

Precisamos ter a mesma quantidade de valores e variaveis, pois faltando um ou outro da erro.
Porem, suponhamos que eu tenha um lista com 5 nomes, ai eu desempacoto fazendo nome1, nome2 ...
So que eu so quero pegar o 1 nome. Ai eu posso empacotar o resto usando: * junto com alguma variavel que
eu criei. Ex: *resto

Porém caso eu não vou usar essa variavel resto, posso substituir por _. Pois nao e interessante
definir variavel que nao vai ser utilizada
"""
#Desempacotando

listanomes = ["Carlos", 'Antonia', "Francisco", "Thaynna", "Cleiton"]
nome1, nome2, nome3, nome4, nome5 = listanomes

print(nome3)

# Podemos ja tambem fazer assim abaixo:
# nome1, nome2, nome3, nome4, nome5 = ["Carlos", 'Antonia', "Francisco", "Thaynna", "Cleiton"]

# Agora se eu quiser pegar apenas o 1 nome e empacotar o resto eu faço assim, desses 2 jeitos abaixo:

_, _, _, _, nome5, *restante = listanomes 
print(nome5, restante)

nome1, *_ = listanomes
print(nome1, _)

