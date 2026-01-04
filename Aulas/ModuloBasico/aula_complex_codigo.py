"""
Aula falando sobre complexidade de codigo, boas praticas e como pensar para escrever programas
para outras pessoas e não para o computador.

Variaveis com letras Maiusculas significam que elas nao vao mudar ao longo do programa = Constantes.
Muitas condições dentro de if = ruim
Quanto mais blocos de codigos afastados da margem = contagem de complexidade = ruim

"""

velocidade_carro = 61   # velocidade atual do carro
local_carro = 100   # local que o carro esta na estrada

RADAR_1 = 60    # Velocidade maxima do radar 
lOCAL_1 = 100   #local onde o radar 1 esta
RADAR_RANGE = 1     # a distancia onde o radar pega

# Verificar se o carro passou da velocidade do radar sem boas praticas.
# if velocidade_carro == RADAR_1:
#     print("O carro passou na velocidade do radar")

# elif velocidade_carro != RADAR_1:
#     print("A velocidade do carro passou do limite do radar1")

# Verificar se o carro foi multado ou não pelo radar com boas praticas
range_menor = (lOCAL_1 - RADAR_RANGE)
range_maior = (lOCAL_1 + RADAR_RANGE)

velocidade_carro_radar = velocidade_carro > RADAR_1
carro_no_radar = local_carro >= (range_menor) and local_carro <= (range_maior)
carro_multa = carro_no_radar and velocidade_carro_radar

if velocidade_carro_radar:
    print("O carro passou da velocidade do radar.")

if carro_no_radar:
    print("O carro passou pelo local do radar.")

if carro_multa:
    print("O carro foi multado")
