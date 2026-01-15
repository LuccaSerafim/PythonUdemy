"""
Aula de range com o for
o Range vai ser o segundo iteravel que vamos aprender
O range nao depende de nada do for, assim como o for nao depende de nada do range.
Tomar cuidado para nao definir variaveis com algo que o proprio python ja tem, Ex: range = range().


O range tem 3 'valores' digamos assim: range(start,stop,step). Podemos passar so um valor caso quisermos.
Porém se passamos apenas um valor, esse valor é o de stop, pois iniciamos em 0 por exemplo e paramos no numero
que passamos no range. Ex: range(10). Nesse caso ele começa em 0 e vai ate 9 pois o ultimo valor nao e incluido.
No caso de range(1,10) , eu defino o start em 1 e vamos ate 9 pois 10 não entra.
Para o caso do step estamos definindo de quantos em quantos vamos pular. Ex: range(1,10,3).
Podemos ter o step negativo também, mas temos que pensar que se queremos que ele conte negativamente
precisamos botar o/os numeros negativo para que ele possa fazer a conta "voltando".

"""
# Exemplo usando range, pensei em falar se os numeros são impares ou pares no range
numeros = range(0, 100)

for impar_par in numeros:
    if (impar_par % 2 == 1):
        print(impar_par,"é impar!")
    else:
        print(impar_par,"é par!")