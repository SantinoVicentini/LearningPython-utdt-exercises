import csv
from typing import List, Dict, Tuple, Set, TextIO
from arbol import Arbol

class DataSetArboreo:
    def __init__(self, filename:str):
        '''Lee el archivo csv que contiene todos los arboles.'''
        self.arboles:List[Arbol] = []
        f:TextIO = open(filename, encoding="utf-8")
        
        linea:Dict[str,str]    
        for linea in csv.DictReader(f):
            longitud:float = float(linea['long'])
            latitud:float = float(linea['lat'])
            nombre:str = linea['nombre_cie']
            barrio:str = linea['barrio']
            id_arbol:int = int(linea['id_arbol'])
            calle:str = linea['calle']
            chapa1:int = int(linea['chapa1'])
       
            arb:Arbol = Arbol(longitud, latitud, nombre, barrio, id_arbol, calle, chapa1)
            self.arboles.append(arb)
            
            
        f.close()
        

    def tamano(self) -> int:
        '''Precondicion: Ninguna.
        Postcondicion: Devuelve la cantidad total de arboles en el dataset d.'''
        return len(self.arboles)
    
    def especies(self) -> set[str]:
        '''Precondicion: Ninguna. 
        Postcondicion: Devuelve todas las especies de los árboles del dataset d.'''
        especies:Set[str] = set()
        i:int = 0
        while i < len(self.arboles):
            agrega_especie = self.arboles[i].especie
            especies.add(agrega_especie)
            i = i + 1  
        return especies
    
        
    def barrios(self) -> set[str]:
        '''Precondicion: Ninguna 
        Postcondicion: Devuelve el conjunto de barrios de todos los arboles en el dataset.
        '''
        barrios:Set[str] = set()
        i:int = 0
        while i < len(self.arboles):
            barrios.add(self.arboles[i].barrio)
            i = i + 1
        return barrios
    
        
    def arboles_de_la_especie(self, especie:str) -> List[Arbol]:
        '''Precondicion: Ninguna.
        Postcondicion: Devuelve todos los arboles en el dataset que tienen la especie indicada.'''
        vr:List[Arbol] = []
        i:int = 0 
        while i < len(self.arboles):
            if especie == self.arboles[i].especie:
                vr.append(self.arboles[i])
            i = i + 1
        return vr
                   #O(1)

    def TotalArboles(self) -> List[str]:
        '''Precondicion: Ninguna.
        Postcondicion: El valor de retorno seran todas las especies de arboles con sus repetidos en self.arboles.'''
        total_arboles:List[str] = []
        i:int
        for i in range(len(self.arboles)):
            total_arboles.append(self.arboles[i].especie)
        return total_arboles

    def cantidad_por_especie(self, minimo:int) -> Dict[str, int]:
        '''Devuelve la cantidad de ejemplares de cada especie existente en el dataset d. incluyendo
        solamente a las especies que tienen como mínimo la cantidad de ejemplares indicada.
        Por ejemplo, para el dataset
        completo del archivo CSV, d.cantidad_por_especie(20000) devuelve este diccionario:
            { 'Melia azeradach': 24558,
             'Platanus x acerifolia': 34786,                #COMPLEJIDAD O(N*M)
             'Ficus benjamina': 23907
             'Fraxinus pennsylvanica': 141825 }'''

        dict_cant:Dict[str, int] = dict()
        arboles:List[str] = self.TotalArboles()
        
        arbol:str
        for arbol in arboles:
            if arbol in dict_cant:
                dict_cant[arbol] += 1
            else:
                dict_cant[arbol] = 1
        vr:Dict[str, int] = dict()
        clave:str        
        for clave in dict_cant:
            if dict_cant[clave] >= minimo:
                vr[clave] = dict_cant[clave]
                
        return vr

    def arbol_mas_cercano(self, especie:str, lat:float, lon:float) -> str:
        '''d.arbol_mas_cercano(especie:str, lat:float, lng:float): Devuelve el árbol de
        la especie indicada que está más cercano al punto hlat, lngi en el dataset d, usando la distancia euclidiana.
        Este método tiene como precondición que exista al menos un árbol de dicha especie en el dataset d. 
        Por ejemplo, considerando el dataset completo del archivo CSV,
        d.arbol_mas_cercano('Citrus aurantium', -34.55472, -58.44583) devuelve el naranjo más cercano a la Di Tella, el cual tiene número 
        identificador 55001143 y dirección “Garcia, Manuel J., Alte. 923”.'''
        
        
        listaDeArbolesEspecie:List[Arbol] = self.arboles_de_la_especie(especie)
        distancia_minima:float = listaDeArbolesEspecie[0].distancia(lat,lon)
        arbol:Arbol
        for arbol in listaDeArbolesEspecie:
            if arbol.distancia(lat,lon) <= distancia_minima:
                distancia_minima = arbol.distancia(lat,lon)
                arbolMasCercano = arbol
                
        return f'Arbol(id = {arbolMasCercano.id}) {arbolMasCercano.direccion()}, {arbolMasCercano.barrio}'

    
dataset = DataSetArboreo('arbolado-publico-lineal.csv')
print(dataset.cantidad_por_especie(40))
#print(dataset.arbol_mas_cercano('Citrus aurantium', -34.55472, -58.44583))
#print(dataset.arbol_mas_cercano('Citrus aurantium', -34.55472, -58.44583))

#print(dataset.tamano())
#print(dataset.especies())
#print(dataset.TotalArboles())
#print(dataset.arboles_de_la_especie('Acer negundo'))






