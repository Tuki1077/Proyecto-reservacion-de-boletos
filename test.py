import unittest
import functions as fn
import numpy as np

class test_funciones (unittest.TestCase):
    # def avion (self):
    #     self.lista = np.array([
    #         ["","A","B","C","D","E","F"],
    #         ["1","0","0","0","0","0","0"],
    #         ["2","0","0","0","0","0","0"],
    #         ["3","0","0","0","0","0","0"]
    #     ])

    # def test_asignar_boleto (self):
    #     self.assertEqual(fn.reservar_boleto(self.lista, 2, 3), "X")

    def test_translate (self):
        self.assertEqual(fn.translate_to_number("A"), 1)