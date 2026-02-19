"""
Aula sobre closure e funções que retornam outras funções.

Uma closure acontece quando uma função "interna" consegue lembrar e acessar variáveis da função "externa", 
mesmo depois que a função externa já terminou de executar. É como se a função interna carregasse 
uma "mochila" com as variáveis que ela precisa.

Cada closure mantém sua própria "memória" das variáveis.

O closure é bom para:

Criar funções personalizadas
Manter dados privados (encapsulamento)
Evitar variáveis globais
Criar decorators.


Relembrando as high order functions:

São funções que fazem pelo menos UMA dessas coisas:
Recebem outra função como parâmetro, OU
Retornam uma função como resultado

Se uma função faz qualquer uma dessas coisas, ela é uma high-order function.

"""

def função_externa(mensagem):
    # Esta é a variável da função externa
    
    def função_interna():
        # A função interna "lembra" da variável mensagem
        print(mensagem)
    
    return função_interna

# Criando closures
saudacao = função_externa("Olá!")
despedida = função_externa("Tchau!")

saudacao()  # Imprime: Olá!
despedida() # Imprime: Tchau!