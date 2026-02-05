"""
Aula falando sobre o retorno de valores da função (return)

Algumas funções não retornam um valor útil, por exemplo, retornam None, como o print(). Ao usar a palavra return,
fazemos com que a função retorne um valor específico.

Basicamente o return é como se fosse uma resposta de uma pergunta que você fez.

Somente as funções e métodos tem a palavra return.

Tudo que escrevemos após o return, o python mostra que esta inacessivel, ou seja, ele vai executar o codigo, chegou
no return ele vai parar ali e acabou

Não confudir return com print, o print ele mostra o valor na tela e acabou, o return ele devolve esse valor
que voce quer e voce decide se usa ou não.
"""


def aula_return():
    frase = "Isso é um teste para testar o return"

    if len(frase) > 20:
        return "É maior"
    
    return "É menor"


print(aula_return())