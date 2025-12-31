"""
Aula sobre o operador logico AND
No and todas as condições precisam ser verdadeiras
Sao considerados falsy: 0 , 0.0 , ""(string vazia sem espaços.) e False. OBS: Caso confronte algum desse com bolean o resultado da False
Todas as condiçoes precisam ser verdadeiras.
Podemos ter várias condições And no mesmo codigo
Caso um valor seja considerado falso, a expresao inteira sera avalidado naquele valor
Caso temos varias condições onde no meio delas tem um False, o codigo para naquele ponto 
e nao checa o resto pra frente
Tambem tem o tipo None(não valor) que basicamente e considerado um valor que nao existe
Caso temos varias condições ali e dependendo da condição que ele parar, pode ser que ele retorne a propria condição que parou
EX: print(True and 0 and True)
Exemplo de sistema com AND:
"""
# Exemplo 1 com sistemas
login = input('[E]ntrar [S]air: ')
senha = input('Crie uma senha: ')

linha = 20 * "-"
print(linha)

senha_aceita = input("Entre com sua senha: ")

if login == "E" and senha == senha_aceita:
    print("Parabéns voce entrou na sua conta")


elif login == "S":
    print("Você saiu do sistema")

if login == "E" and senha != senha_aceita:
    print("Você digitou a senha errada, por favor tente novamente")

# Exemplo avaliação curto circuito
# print(True and 0 and True)
# print(bool(''))


