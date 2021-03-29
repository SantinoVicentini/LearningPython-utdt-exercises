def misma_paridad(n:int, m:int) -> bool:

    if n % 2 == 0 and m % 2 == 0 or n % 2 == 1 and m % 2 == 1: 
        vr = True

    else: 
        vr = False  
    
    return vr

import unittest

class Misma(unittest.TestCase):

#   A PARTIR DE ACA USTEDES ESCRIBAN LOS TEST
    
    def test_verdaderos(self):
        self.assertTrue(misma_paridad(2,2))
        self.assertTrue(misma_paridad(3,9))
        #NUEVO TEST
        
        
    def test_falsos(self):
        self.assertFalse(misma_paridad(2,3))
        #NUEVO TEST

# esta linea es para correr los test previamente declarados
unittest.main()
