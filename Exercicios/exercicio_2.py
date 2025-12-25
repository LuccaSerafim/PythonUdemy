# Exercicio 2 é sobre o calculo de IMC. o IMC é calculado com peso/(altura x altura)
# O exercicio pede para fazer o calculo de imc e imprimir: Nome, altura, peso e o Imc

nome = "Lucca"
altura = 1.82
peso = 65
imc = peso / (altura ** 2)

print( nome, 'tem', altura, "de altura" ,end=',\n')
print('pesa',peso,"quilos", 'e seu IMC é', end=':\n')
print(imc)