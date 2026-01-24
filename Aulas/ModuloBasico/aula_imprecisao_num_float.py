"""
Aula falando sobre a imprecisão de numeros float no python

O python, entre outras linguagens tbm, acaba não arredondando os numeros de float automaticamente.
EX: num1 = 0.1 | num2= 0.7 | soma = num1 + num2 
se dermos um print(soma) o resultado que temos é 0.79999... 

Um jeito de arredondar é formatando o resultado final, por exemplo, f-strings : 
print(f"{soma:.2f}").

Temos tbm a função round() , onde passamos o que queremos arredondar e tambem a quantidade de casas decimais:
print(round(soma, 1)). Ele acaba cortando os 0.

Temos tambem um outro jeito, usado mais em casos especificos, que é um módulo do python chamado:
decimal. Onde fazemos o import dele e usamos a função decimal.Decimal().
Ao usar essa função geralmente passamos uma string nele e ele proprio converte para o que precisamos (nesse exemplo
o float)


"""
import decimal

num3 = decimal.Decimal("0.1")
num4 = decimal.Decimal("0.7")
soma1 = num3 + num4
print(soma1)

num1 = 0.1
num2= 0.7
soma2 = num1 + num2
print(soma2)
print(f"{soma2:.2f}")
print(round(soma2, 1))
