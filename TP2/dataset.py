import csv
from typing import List, Dict, Tuple, Set, TextIO
from arbol import Arbol

class DataSetArboreo:
    def __init__(self, filename:str):
        self.arboles:list[Arbol] = []

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

    def TotalArboles(self) -> List[str]:
        i:int
        vr:List[str] = []
        for i in range(len(self.arboles)):
            vr.append(self.arboles[i].nombre)
        return vr

    def cantidad_por_especie(self) -> Dict[str,int]:
        dict_cant:Dict[str, int] = dict()
        arboles:List[str] = self.TotalArboles()
        arbol:str
        for arbol in arboles:
            if arbol in dict_cant:
                dict_cant[arbol] += 1
            else:
                dict_cant[arbol] = 1
                
        return dict_cant
    
dataset = DataSetArboreo('arbolado-publico-lineal.csv')
print(dataset.cantidad_por_especie())
#print(dataset.tamano())
#print(dataset.especies())
#print(dataset.barrios())
#print(dataset.arboles_de_la_especie('Acer negundo'))






