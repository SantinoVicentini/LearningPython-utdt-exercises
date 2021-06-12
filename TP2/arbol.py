from typing import List, Dict, Set, TextIO
class Arbol:
    def __init__(self, lat:float, lon:float, esp:str, barr:str, ID:int, call:str, chap1:int):
        ''' Inicializa cada arbol con los atributos latitud lat, longitud lon, especie esp, barrio barr
        id ident, calle call y chapa1 chap1.'''
        ...
        self.latitud = lat
        self.longitud = lon
        self.especie = esp
        self.barrio = barr
        self.id = ID
        self.calle = call
        self.chapa1 = chap1 
        
    def __repr__(self):
        '''Devuelve la representacion a strdel id de cada Arbol.'''
        return f'Arbol(id={self.id})'
 
    def direccion(self) -> str:
        '''Devuelve la dirreccion del arbol consultado.'''
        return self.calle + ' ' + str(self.chapa1)
    
    def distancia(self, lat:float, lon:float) -> float:
        '''Devuelve la distancia entre las coordenadas ingresadas y el Arbol consultado. '''
        ...
        return (((lat - self.longitud)**2) + ((lon - self.latitud)**2))**0.5



a:Arbol = Arbol(34.6200256156, 58.3890587967,'Fraxinus pennsylvanica',
          'CONSTITUCION', 2430, 'Calvo, Carlos', '1609')
print(a.distancia(-34.6200256156, -58.3890587967))
print(a.distancia(34.6200256156, 58.3890587967))
print(a.distancia(0, 0))
print(a.distancia(-34.6200256156, -58.3890587967))


