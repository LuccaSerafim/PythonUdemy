"""
Aula falando sobre as precedencias dos operadores vistos, onde ele vai seguir uma ordenzinha do que executar primeiro

1. (n + n) 
OBS: Caso tenha parenteses dentro de parenteses, o mais interno vai ser executado primeiro e assim por diante.
O famoso de dentro para fora

2. ** --> exponenciação
3. * / // % --> multiplicação, as divisões e o modulo
4. + - --> soma e subtração

OBS: Caso temos operadores de mesma precedencia na conta, ex: * e /, ela vai ser realizado primeiro da esquerda para a direita

"""

exemplo_conta1 = 2 + 8 ** 2 + 7
exemplo_conta2 = (2 + 8) ** (2 + 7)
print(exemplo_conta1)
print(exemplo_conta2)
