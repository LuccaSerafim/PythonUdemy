"""
Aula breve introdutoria de formatação de strings, exemplo da aula do curso: exercicio de imc
Exemplo: caso queira exibir certinho igual do exercicio, botar um f na frente e envolver a/as variaveis em {}
Ex: linha_1 = f'{nome} tem altura de altura'
Tem a possibilidade de formatar tambem na variavel que tem as chaves, exemplo caso eu queria mostrar minha altura 
com as casas decimais fazemos assim: linha_1 = f'{nome} tem {altura:.2f} de altura' 
Esse .2f me diz quantas casas decimais vai mostrar
Da para botar virgula tambem ao lado desse . 
Ex: {altura:,.2f} . Mais usado no caso de valores de dinheiro, vou fazer o exemplo com a altura mesmo
"""

nome = 'Lucca'
altura = 1.82
peso = 65
imc = peso / (altura ** 2)

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print( linha_1)
print(linha_2)
print(linha_3)
