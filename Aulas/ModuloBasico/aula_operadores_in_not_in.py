"""
Aula falando sobre os operadores: in e not in
(in = estar entre) e (not in = nao estar entre)
lembrando que strings em python sao iteraveis(podendo navegar item por item)
e podemos navegar por elas por indices por exemplo. Lembrando que indices positivos começam no 0
Acessamos os indices atraves de []


"""

esportes = "Basquete", "Vôlei", "Baseball", "Tenis" ,"Skate" 
encontrar_esportes = input("Digite qual esporte quer encontrar da lista: ")

if encontrar_esportes in esportes :
    print(f'{encontrar_esportes} esta na lista')


elif encontrar_esportes not in esportes: 
    print(f"{encontrar_esportes} não esta na lista")