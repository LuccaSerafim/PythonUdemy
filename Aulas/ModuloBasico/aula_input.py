# Aula da função input, o usuário interage com o código
# Ao rodar, o programa so para quando o usuario digita algo, mesmo se for so um enter
# A função input torna o valor recebido em string, qualquer coisa fazer a coersão para a string
# Nesse exemplo de codigo onde eu ja converto o peso e a altura em int e float, caso eu digite uma string o codigo ja da erro
# Por isso o correto seria fazer uma checagem e aparecer na tela do usuario que tem que digitar um numero mesmo e nao uma string



nome = input('Qual o seu nome?')
peso = input("Quanto voce pesa? (em KG)")
altura = input("Qual a sua altura? (em Metros)")

peso_correto = int(peso)
altura_correto = float(altura)
imc = peso_correto / altura_correto ** 2

print(f" O seu nome é{nome}, você pesa {peso_correto} kg, sua altura é {altura_correto:.2f}, seu imc é {imc:.2f}") 