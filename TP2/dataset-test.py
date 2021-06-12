import unittest

# Importamos el codigo a testear.
from dataset import DataSetArboreo


####################################################################

class TestDataSetArboreo(unittest.TestCase):

    def setUp(self):
        self.dataset: DataSetArboreo = DataSetArboreo(
            filename='arbolado-publico-lineal.csv'
        )
        
    def test_tamano(self):
        self.assertEqual(self.dataset.tamano(), 50)
        
    def test_especies(self):
        self.assertEqual(self.dataset.especies(), {'Bauhinia forticata', 'Prunus cerasifera', 'Ficus benjamina', 'Ligustrum lucidum', 'Robinia pseudoacacia',
         'Acer negundo', 'Fraxinus pennsylvanica', 'Tilia viridis subsp. x moltkei'})

    def test_barrios(self):
        self.assertEqual(self.dataset.barrios(), {'CONSTITUCION'})

    def test_arboles_de_la_especie(self):
        #especies repetidas
        #self.assertEqual(self.dataset.arboles_de_la_especie('Acer negundo'),[]) ?? no se como hacer para comparar esto

        #especie que no se encuentra en el csv
        self.assertEqual(self.dataset.arboles_de_la_especie('Liquidambar  styraciflua'),[])
    
    def test_total_arboles(self):
        self.assertEqual(self.dataset.TotalArboles(), ['Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Ligustrum lucidum', 'Acer negundo', 'Fraxinus pennsylvanica', 'Prunus cerasifera', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Ficus benjamina', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica',
         'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Tilia viridis subsp. x moltkei', 'Fraxinus pennsylvanica', 'Ficus benjamina', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Robinia pseudoacacia', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Fraxinus pennsylvanica', 'Bauhinia forticata', 'Bauhinia forticata'])

    def test_cantidad_por_especie(self):
        #no vacío
        self.assertEqual(self.dataset.cantidad_por_especie(40), {'Fraxinus pennsylvanica': 41})
        #vacío
        self.assertEqual(self.dataset.cantidad_por_especie(50), {})

    def test_arbol_mas_cercano(self):
        #prueba con csv completo
        self.datasetCompleto: DataSetArboreo = DataSetArboreo(
            filename='arbolado-publico-lineal-2011.csv'
        )
        self.assertEqual(self.datasetCompleto.arbol_mas_cercano('Citrus aurantium', -34.55472, -58.44583), 'Arbol(id = 55001143) Garcia, Manuel J., Alte. 923, BELGRANO')
        

## y así con el resto de los métodos a testear.
        
####################################################################

unittest.main()
