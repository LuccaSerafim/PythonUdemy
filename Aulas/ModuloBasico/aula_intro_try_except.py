"""
Aula introdutoria de try e except
Try = tentar executar o codigo
Except = ocorreu algum erro ao executar o codigo
OBS: O erro não e de sintaxe assim, o codigo esta bonitinho sem erros de escrita

Sempre que o usuaria te passar algum valor, temos que tratar esse valor
Na aula ele fez exemplo com isdigit, que verifica se o usuario digitou APENAS NUMEROS,
se o usuario der um . ja da erro. isdigit retorna um bool(True ou False)
Erros são chamado de excessoes no python.
O if não evita excessoes, ele apenas verifica a logica por tras.
O try e except lembra um if else, so que caso de erro no try ele pula direto pro except.
Não e muito prudente usar o try except igual no exemplo que ele deu na aula.
"""

# Código da aula pois fiquei com preguiça em pensar em algo
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')