from guia5v2 import primo
#defino
i:int = 0
cant:int = 0
while i <= 100:
    #si es primo lo imprimo
    if primo(i):
        print(i)
    i+=1
    