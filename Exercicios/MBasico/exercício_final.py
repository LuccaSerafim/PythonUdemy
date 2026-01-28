"""
Exercício Final do Módulo Básico: Validador de cpf. 

Esse exercicio pega desde a aula 99 ate a 104, pois cada uma dessas aulas vao falar sobre algo do exercicio.
Nessa primeira aula (99) vamos validar o 1° digito de um cpf aleátorio.

OBS: Esse cpf aléatorio vem de um gerador de cpf online totalmente legal, não veio da receita federal, é apenas
para verificar se esse possivel cpf é válido ou não.

A estrutura do calculo para verificar os digitos do cpf é:

# Calculo do 1° digito:
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

#Calculo do 2° digito:
Inves de pegar os nove primeiros agora, pegamos os 10
Multiplicando cada um dos valores por uma contagem regressiva começando de 11.
Depois o resto e igual, soma os resultados, multiplica por 10, pega esse resultado e ve o resto
da divisao por 11, e se for maior que 9 é 0 e se for menor o resultado é ele mesmo

# OBS: Temos alguns problemas onde vi como concertar na Aula de possiveis problemas e a soluções para esses problemas
desse exercicio aqui

"""
cpf_para_verificacao = "74682489070" #Cpf ficticio para verificar
tamanho_cpf_d1 = cpf_para_verificacao[:9] 
contador_regressivo_d1 = 10 

resultado_digito1 = 0


for digito in tamanho_cpf_d1:
    resultado_digito1 += int(digito) * contador_regressivo_d1 
    contador_regressivo_d1 -= 1


digito1 = (resultado_digito1 * 10) % 11 
digito1 = 0 if digito1 > 9 else digito1
# print(digito1) # Descomente esse print caso queira ver o 1° digito

tamanho_cpf_d2 = tamanho_cpf_d1 + cpf_para_verificacao[9]
contador_regressivo_d2 = 11

resultado_digito2 = 0

for digito2 in tamanho_cpf_d2:
    resultado_digito2 += int(digito2) * contador_regressivo_d2
    contador_regressivo_d2 -= 1

digito2 = (resultado_digito2 * 10) % 11
digito2 = 0 if digito2 > 9 else digito2
# print(digito2) # Descomente aqui caso queira ver o 2° digito

cpf_pelo_calculo = f"{tamanho_cpf_d1}{digito1}{digito2}"
# print(cpf_pelo_calculo) # Descomente caso queira ver o cpf gerado por esse codigo

if cpf_para_verificacao == cpf_pelo_calculo:
    print(f"O cpf {cpf_para_verificacao} é um CPF Válido")
else:
    print("CPF Inválido")





   
    




    

    




 



 