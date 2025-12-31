"""
Aula sobre o operador logico or
Tem os mesmo valores falsy do and
Qualquer condição verdadeira vai avaliar toda a expressao como verdadeira
Se qualquer valor for considerado como verdadeiro a expressão inteira
sera avaliado naquele valor
Caso temos uma expressão que tem or e and na mesma expressaão, ela pode ficar ambigua.
Temos a avaliação de curto circuito tbm
"""
# Exemplo: fazer a entrada com e(minusculo)

login = input('[E]ntrar [S]air: ')
senha = input('Crie uma senha: ')

linha = 20 * "-"
print(linha)

senha_aceita = input("Digite sua senha: ")

if (login == "E" or login == 'e') and senha == senha_aceita:
    print("Parabéns voce entrou na sua conta")


elif login == "S":
    print("Você saiu do sistema")

elif (login == "E" or login == 'e') and senha != senha_aceita:
    print("Você digitou a senha errada, por favor tente novamente")

# Avaliação curto circuito

# senha = input("senha: ") or "Não digitou nada"
# print(senha)

