"""
Ultima aula do Modulo Basico, conectando ainda com o Exercicio Final do Modulo.

Essa aula vai ser de Gerar um cpf aleatorio.
No caso ele ensinou mais um módulo que é o Random, e dentro desse random temos o randint().
Onde temos que passar de qual numero queremos começar ate qual queremos terminar.

"""

import random

cpf = ""

for i in range(9):
   cpf += str(random.randint(0,9))

print(cpf)

# Aqui seria interessante ver se o cpf é valido ou não igual no nosso exercicio

cpf_para_verificacao = cpf

contador_regressivo_d1 = 10 

resultado_digito1 = 0


for digito in cpf_para_verificacao:
    resultado_digito1 += int(digito) * contador_regressivo_d1 
    contador_regressivo_d1 -= 1


digito1 = (resultado_digito1 * 10) % 11 
digito1 = 0 if digito1 > 9 else digito1

print(digito1)

tamanho_cpf = cpf_para_verificacao + str(digito1)

contador_regressivo_d2 = 11

resultado_digito2 = 0

for digito2 in tamanho_cpf:
    resultado_digito2 += int(digito2) * contador_regressivo_d2
    contador_regressivo_d2 -= 1

digito2 = (resultado_digito2 * 10) % 11
digito2 = 0 if digito2 > 9 else digito2

print(digito2)

cpf_pelo_calculo = f"{cpf_para_verificacao}{digito1}{digito2}"
print(cpf_pelo_calculo) # Descomente caso queira ver o cpf gerado por esse codigo

if cpf_pelo_calculo == cpf_pelo_calculo:
    print(f"O cpf {cpf_pelo_calculo} é um CPF Válido")
else:
    print("CPF Inválido")

# Código ficou meio repetitivo, porem foi usando apenas as coisas que vi nesse Módulo Básico, mais pra frente eu melhoro
