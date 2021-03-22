#Ejercicio de la clase practica n3

#NO ES NECESARIO QUE SEPAN CÓMO FUNCIONA nueva_bodega PERO SI QUÉ HACE

import unittest

def nueva_bodega(s:str) -> bool:
    vino:str='vino'
    bodega:str='bodega'
    nueva:str='nueva'
    
    vr:bool= nueva in s or vino in s or bodega in s 
    
    return vr



#   ACA EMPIEZAN LOS TEST 

class TestNuevaBodega(unittest.TestCase):

#   A PARTIR DE ACA USTEDES ESCRIBAN LOS TEST
    
    def test_verdaderos(self):
        self.assertTrue(nueva_bodega('nueva bodega'))
        self.assertEqual(nueva_bodega('nuevas vinotecas abren en la ciudad, venga por su vino'), True)
        #NUEVO TEST
        
        
    def test_falsos(self):
        self.assertFalse(nueva_bodega('tengo un nuevo libro en mi biblioteca'))
        #NUEVO TEST

# esta linea es para correr los test previamente declarados
unittest.main()
