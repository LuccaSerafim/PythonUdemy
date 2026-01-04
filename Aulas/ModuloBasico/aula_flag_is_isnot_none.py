"""
Aula falando sobre Flags, is, is not e none
Flag = Demarcar um local
Is e Is not = é ou não é (tipo, valor, identidade)
None = Não Valor
Geralmente usamos o none com is
Sempre que estiver com o not na frente  esta invertendo o valor da coisa
A flag e como se fosse uma bandeira, ai junto com o none a gente pode fincar ela ou não.

Uma pratica ruim é declarar coisas dentro de blocos de codigo(if) para usar fora desse bloco
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')