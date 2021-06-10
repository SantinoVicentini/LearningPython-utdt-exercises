import csv
from typing import List, Dict, Tuple, Set
from arbol import Arbol

class DataSetArboreo:
    def __init__(self, filename:str):
        self.arboles:list[arbol] = []

        # Importamos los usuarios primero
        filename: TextIO = open(filename, 'r', encoding='utf-8')
        linea: Dict[str, str]
        for linea in csv.DictReader(filename):
            # Tomo los datos y los convierto a int
            idArbol:int = int(linea['id_arbol'])
            latitud:float = float(linea['lat'])
            longitud:float = float(linea['long'])
            nombre:str = linea['nombre_cie']
            barrio:str = linea['barrio']
            calle:str = linea['calle']
            chapa1:int = int(linea['chapa1'])

    
            # Creo el usuario y lo almaceno
            arbol:arbol = Arbol(idArbol, longitud, latitud, nombre, barrio, calle, chapa1)
            # COMPLETAR
            self.arboles.append(arbol)
            
        
        filename.close()

    def tamano(self) -> int:
        return len(self.arboles)

    def especies(self) -> Set[str]:
        especies:Set[str] = set()
        i:int = 0
        while i < len(self.arboles):
            especies.add(self.arboles[i].nombre)
            i+=1
        return especies

    def barrios(self) -> Set[str]:
        barrios:Set[str] = set()
        i:int = 0
        while i < len(self.arboles):
            barrios.add(self.arboles[i].barrio)
            i+=1
        return barrios

    def arboles_de_la_especie(self, especie:str) -> List[Arbol]:
        vr:List[Arbol] = []
        i:int = 0
        while i < len(self.arboles):
            if especie == self.arboles[i].nombre:
                vr.append(self.arboles[i])
            i+=1
        return vr



    

    
dataset = DataSetArboreo('arbolado-publico-lineal.csv')
print(dataset.tamano())
print(dataset.especies())
print(dataset.barrios())
print(dataset.arboles_de_la_especie('Acer negundo'))




