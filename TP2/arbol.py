from typing import List, Dict, Set, TextIO
import math
class Arbol:
    def __init__(self, ident:int, lon:float, lat:float, nom:str, barr:str, calle:str, chap:int):
        self.latitud = lat
        self.longitud = lon
        self.id = ident
        self.nombre = nom
        self.barrio = barr
        self.calle = calle
        self.chapa1 = chap

    def direccion(self) ->str:
        return self.calle + ' ' + str(self.chapa1)

    def distancia(self, lat:float, lon:float) -> float:
        return math.sqrt(((self.longitud - lon)*2) + ((self.latitud - lat)*2))

    def __repr__(self):
        return f'Arbol(id={self.id})'



