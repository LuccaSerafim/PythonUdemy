# Essa aula é entendendo mais sobre os condicionais if, elif e else
#  Relembrando: podenos ter o if funcionando sozinho, porem elif e else dependem do if
# Caso temos que fazer varias condiçoes, podemos usar so 1 if e o resto usa elif
# Caso temos varios blocos de condiçoes que são False o python vai percorrer todas ate achar uma True ou ate achar um else
# Lembrar que a primeira checagem vai ser um if, e podemos ter varios blocos de checagem um dentro do outro
# Caso tenha varios blocos de checagem lembrar de identar certinho pois se estiver errado ele vai checar outro bloco que voce nao quer


pergunta = input("Você gostou de Stranger Things? (Responda com Sim, Não ou Mais ou menos) ")


if pergunta == "Sim":
    print('Eu também gostei')

elif pergunta == "Não":
    pergunta2 = input("Mas do que você não gostou? (responda com: Os personagens novos, o enredo ou o vecna não morreu) ")
    
    if pergunta2 == "Os personagens novos": 
        print("Eles poderiam ser melhores mesmo")

    elif pergunta2 == "o enredo":
        print("Essa ultima temporada foi estranho mesmo")

    elif pergunta2 == 'o vecna não morreu':
        print("Era pra ele ter morrido mesmo.")


elif pergunta == "Mais ou menos":
    print("Não gostou da ultima temporada ne?")

else:
    print('Reassiste que voce vai gostar.')
