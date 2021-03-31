
import unittest

from peculiar import misma_paridad
from peculiar import alterna_paridad
from peculiar import es_peculiar

class Misma(unittest.TestCase):

#   A PARTIR DE ACA USTEDES ESCRIBAN LOS TEST
    
    def test_verdaderos(self):
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
        self.assertFalse(misma_paridad(2,3))
        #Alterna Paridad
        self.assertFalse(alterna_paridad(123455))
        #Es Peculiar
        self.assertFalse(alterna_paridad(1079))

        #NUEVO TEST

# esta linea es para correr los test previamente declarados
unittest.main()
