from typing import TextIO

#t:TextIO = open('C:\\Users\\Santino\\Downloads\\provincias.csv', encoding='utf-8')

#texto:str = t.read()
#print(len(texto))

#linea:str
#for linea in t:
#    linea = linea.rstrip()
#    valores:list[str] = linea.split(',')
#   print(valores[0])

#f:TextIO = open('20pimeros.txt', 'w', encoding='utf-8')

#x:str
#for x in range(1,21):
#    f.write(str(x) + '\n')
#f.close()

num:str = input('que numero deseas evaluar?')
numero:int = int(num)

vr:str = 'correcto'
i:int = 1
while i <= 10:
    resultado:str = input('cuanto es ' + str(numero) + ' por ' + str(i) + ' ?')
    resulv2:int = int(resultado)
    if resulv2 == i * numero:
        print(vr)
    if i * numero != resulv2:
        vr = 'incorrecto ' + 'es ' + str(i*numero)
        print(vr)
    i += 1
#Terminar