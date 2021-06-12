import unittest

# Importamos el codigo a testear.
from arbol import Arbol

####################################################################

class TestArbol(unittest.TestCase):

    def test_direccion(self):
        a:Arbol = Arbol(-34.6200256156, -58.3890587967,'Fraxinus pennsylvanica',
          'CONSTITUCION', 2430, 'Calvo, Carlos', '1609')
        b:Arbol = Arbol(-34.6200256156, -58.3890587967,'Fraxinus pennsylvanica',
          'CONSTITUCION', 2430, '', '')
        #No vacío
        self.assertEqual(a.direccion(), 'Calvo, Carlos 1609')
        #Vacío
        self.assertEqual(b.direccion(), ' ')

    def test_distancia(self):
        #Lat y Lon negativas
        a:Arbol = Arbol(-34.6200256156, -58.3890587967,'Fraxinus pennsylvanica',
          'CONSTITUCION', 2430, 'Calvo, Carlos', '1609')
        #Lat y Lon positivas
        b:Arbol = Arbol(34.6200256156, 58.3890587967,'Fraxinus pennsylvanica',
          'CONSTITUCION', 2430, 'Calvo, Carlos', '1609')
        
        #argumentos negativos
        self.assertEqual(a.distancia(-34.6200256156, -58.3890587967), 33.61448908920773)
        self.assertEqual(b.distancia(-34.6200256156, -58.3890587967), 131.53470859977867)

        #argumentos positivos
        self.assertEqual(a.distancia(34.6200256156, 58.3890587967), 131.53470859977867)
        self.assertEqual(b.distancia(34.6200256156, 58.3890587967), 33.61448908920773)

        #argumentos nulos
        self.assertEqual(a.distancia(0, 0), 67.88098673995016)
        self.assertEqual(b.distancia(0, 0), 67.88098673995016)

        #arguments negativo y positivo
        self.assertEqual(a.distancia(-34.6200256156, 58.3890587967), 95.99821207490574)
        self.assertEqual(b.distancia(34.6200256156, -58.3890587967), 95.99821207490574)



    

   # def test_...(self):
    #    ...

    #def test_...(self):
     #   ...

## y así con el resto de los métodos a testear.
        
####################################################################

unittest.main()
