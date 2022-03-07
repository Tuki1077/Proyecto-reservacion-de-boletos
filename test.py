import unittest
import functions as fn
import numpy as np

class test_funciones (unittest.TestCase):

    def test_asignar_boleto (self):
        self.assertEqual(fn.reservar_boleto(np.array( [
    ["","A","B","C","D","E","F"],
    ["1","0","0","0","0","0","0"],
    ["2","0","0","0","0","0","0"],
    ["3","0","0","0","0","0","0"],
    ["4","0","0","0","0","0","0"],
    ["5","0","0","0","0","0","0"],
    ["6","0","0","0","0","0","0"],
    ["7","0","0","0","0","0","0"],
    ["8","0","0","0","0","0","0"]
]), 2, 3),)

    def test_translate (self):
        self.assertEqual(fn.translate_to_number("A"), 1)