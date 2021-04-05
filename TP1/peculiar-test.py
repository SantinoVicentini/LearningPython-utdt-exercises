
import unittest

from peculiar import misma_paridad
from peculiar import alterna_paridad
from peculiar import es_peculiar
from peculiar import n_esimo_peculiar
from peculiar import cant_peculiares_entre



class Misma(unittest.TestCase):

#   A PARTIR DE ACA USTEDES ESCRIBAN LOS TEST
    def test_correctos(self):
        #n_esimo_peculiar
        self.assertEqual(n_esimo_peculiar(1), 418)
        self.assertEqual(n_esimo_peculiar(2), 616)
        #cant_peculiares_entre
        self.assertEqual(cant_peculiares_entre(100, 1000), 6)
        self.assertEqual(cant_peculiares_entre(100, 200), 0)

    def test_verdaderos(self):
        #Misma Paridad
        self.assertTrue(misma_paridad(2,2))
        self.assertTrue(misma_paridad(3,9))
        #Alterna Paridad
        self.assertTrue(alterna_paridad(123450))
        self.assertTrue(alterna_paridad(0))
        #Es Peculiar
        self.assertTrue(es_peculiar(1078))
        self.assertTrue(es_peculiar(0))
        #NUEVO TEST
        
        
    def test_falsos(self):
        #Misma Paridad
        self.assertFalse(misma_paridad(2,3))
        self.assertFalse(misma_paridad(4,5))
        #Alterna Paridad
        self.assertFalse(alterna_paridad(123455))
        self.assertFalse(alterna_paridad(112))
        #Es Peculiar
        self.assertFalse(es_peculiar(1079))
        self.assertFalse(es_peculiar(1))
        #NUEVO TEST

# esta linea es para correr los test previamente declarados
unittest.main()
