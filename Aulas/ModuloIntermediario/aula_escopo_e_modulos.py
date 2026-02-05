"""
Aula sobre escopo de funções e módulos. 

OBS: Essa aula foi dividida em 2 partes (Aulas 109 e 110)

O escopo é o lugar onde o código pode atingir, basicamente significa que o que eu faço dentro da função,
fica dentro dela.

Existe o escopo local e global.

Tudo que estiver definido dentro da função, inclusive os parametros, não consigo acessar fora dela, pois vai dar 
erro mostrando que tal coisa não esta definido

Ex: def aula():
    num1 = 10
    num2 = 20
    soma = num1 + num2
    print(soma)

aula() # ate aqui o codigo roda bonitinho, porem se eu escrever essa linha embaixo:
print(soma) # me traz o erro dizendo que soma não esta difinido

Isso siginifica que a variavel soma esta dentro do escopo da função, e não consigo acessar ela.

Porém o que eu posso fazer é definir a variável fora da minha função e antes de executar ela, pois se eu defino
apos a execução acontece o mesmo erro.

Ex2: def exemplo2():
    fraseconcatenada = "Olá" + palavra
    print(fraseconcatenada)


palavra = "Mundo"
exemplo2()

Agora vamos para a parte mais compicada, que é mostrar o que é do escopo global e o que é do escopo local.

Digamos que eu crie uma variavel qualquer, ai eu crio uma função que imprima essa variavel e dai eu executo
essa função, assim:

qualquer = "Essa frase é do escopo global"

def complicado():
    print(qualquer)

complicado() # Ao executar isso vai me retornar a frase que eu defini acima da função.

Porém se eu crio a mesma variavel dentro da minha função com outro valor para essa variavel e eu chamo ela 
novamente, assim:

def complicado():
    qualquer = "Essa frase é do escopo local"
    print(qualquer)

print(qualquer) #Esse print agora me traz a frase que defini antes da função
complicado() # Esse me traz agora a frase que eu defini dentro da função.

O que acaba sendo diferente pois, mesmo sendo a "mesma" variavel, cada um esta em um escopo diferente, por isso
me devolve frases diferentes.

O que podemos fazer caso queira, é usar a palavra chave do python: global e falar que por exemplo o qualquer
vai ser global agora, não é uma boa prática usar esse global, mas é uma opção.

Só de usar a palavra global com a variavel, faz com que a gente possa pegar do escopo externo e manipular no
escopo interno.

OBS: Vou pegar o trecho de código da aula tambem pois o professor mostrou e usou a global.

"""

def aula():
    num1 = 10
    num2 = 20
    soma = num1 + num2
    print(soma)

aula() # ate aqui o codigo roda bonitinho, porem se eu escrever essa linha embaixo:
# print(soma) # me traz o erro dizendo que soma não esta difinido

def exemplo2():
    fraseconcatenada = f"Olá {palavra}"
    print(fraseconcatenada)


palavra = "Mundo!"
exemplo2()

qualquer = "Essa frase é do escopo global"

def complicado():
    qualquer = "Essa frase é do escopo local"
    print(qualquer)

print(qualquer) #Esse print agora me traz a frase que defini antes da função
complicado() # Esse me traz agora a frase que eu defini dentro da função.

# OBS que eu usei no docstring:
x = 1

def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2     
        print(x, y)
    # Aqui é o escopo mais interno, so aqui eu consigo acessar esse y por exemplo.
# Aqui eu tenho o escopo da função escopo, aqui eu não consigo acessar o escopo da função outra_função.
# Cada função tem seu escopo protegido.
    outra_funcao()
    print(x)

# Aqui fora eu tenho o escopo global, tambem chamado de escopo do módulo, que é basicamente do arquivo python 
# em que estamos.
print(x)
escopo()
print(x)

