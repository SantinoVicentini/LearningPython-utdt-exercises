from typing import List, Tuple, Dict, Set
import math
t : Tuple [int , str]
u : Tuple [int , str]
t = (10 , ' diez ')
u = t
#print ( u [0] , u [1])
t = (20 , ' veinte ')
#print (t , u )
s:Tuple[float, float] = (-1.9, 2.2)
d:Tuple[float, float] = (1.5, 3.3)


#2
#a
def distanciaAlOrigen(xy:Tuple[float,float]) -> float:
    x:float = xy[0] * xy[0]
    y:float = xy[1] * xy[1]
    distancia:float = x + y
    return math.sqrt(distancia)

#print(distanciaAlOrigen(s))

#b
def suma_de_dos_puntos(xy:Tuple[float, float], yx:Tuple[float, float]) -> Tuple[float,float]:
    suma1:float = xy[0] + yx[0]
    suma2:float = xy[1] + yx[1]
    vr:Tuple[float,float] = (suma1, suma2)
    return vr
#print(suma_de_dos_puntos(s, d))

#c
def suma_de_f(xy:Tuple[float, float], f) -> Tuple[float, float]:
    suma1:float = xy[0] + f
    suma2:float = xy[1] + f
    vr = (suma1, suma2)
    return vr
#print(suma_de_f(s, 3.3))

#d
def punto_mas_cercano(xy:Tuple[float, float]) -> Tuple[int, int]:
    red1:int = round(xy[0])
    red2:int = round(xy[1])
    vr:tuple[int,int] = (red1, red2)
    return vr
#print(punto_mas_cercano(s))

#3
def buscar(elem:int, xs:List[int]) -> tuple[bool, int]:
    i:int = 0
    pertenece:bool = False
    vr = (pertenece, None)
    while i < len(xs):
        if elem == xs[i]:
            pertenece = True
            posicion:int = i
            vr:tuple[bool, int] = (pertenece, posicion)
            return vr
        i+=1
    return vr
#print(buscar(5, [3,4,5,5]))

#4

#5




 