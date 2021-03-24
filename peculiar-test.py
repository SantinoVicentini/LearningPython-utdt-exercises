def misma_paridad(n:int, m:int) -> str:

    if n % 2 == 0 and m % 2 == 0 or n % 2 == 1 and m % 2 == 1: 
        print('si')
        return 'si' 

    else: 
        print('no')
        return 'no'     

import unittest

class Misma(unittest.TestCase):

#   A PARTIR DE ACA USTEDES ESCRIBAN LOS TEST
    
    def test_verdaderos(self):
        self.assertEqual(misma_paridad(2,2),'si')
        self.assertEqual(misma_paridad(3,9),'si')
        #NUEVO TEST
        
        
    def test_falsos(self):
        self.assertEqual(misma_paridad(2,3),'no')
        #NUEVO TEST

# esta linea es para correr los test previamente declarados
unittest.main()
