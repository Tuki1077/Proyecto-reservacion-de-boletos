import unittest
import functions as fn
import numpy as np


Avion = np.array( [
    ["","A","B","C","D","E","F"],
    ["1","0","0","0","0","0","0"],
    ["2","0","0","0","0","0","0"],
    ["3","0","0","0","0","0","0"],
    ["4","0","0","0","0","0","0"],
    ["5","0","0","0","0","0","0"],
    ["6","0","0","0","0","0","0"],
    ["7","0","0","0","0","0","0"],
    ["8","0","0","0","0","0","0"]
])
Avion_con_asiento_reservado = np.array ( [
    ["","A","B","C","D","E","F"],
    ["1","X","0","0","0","0","0"],
    ["2","0","0","0","0","0","0"],
    ["3","0","0","0","0","0","0"],
    ["4","0","0","0","0","0","0"],
    ["5","0","0","0","0","0","0"],
    ["6","0","0","0","0","0","0"],
    ["7","0","0","0","0","0","0"],
    ["8","0","0","0","0","0","0"]
])
class test_funciones (unittest.TestCase):

    def test_asignar_boleto (self):
        a=fn.reservar_boleto(Avion, 2, 3)
        self.assertEqual(a, True)
    def test_translate (self):
        self.assertEqual(fn.translate_to_number("A"), 1)
    def test_random(self):
        b = fn.random_for_testing(Avion)
        self.assertEqual(b, True)
    def test_remover_boleto (self):
        c = fn.remover_boleto(Avion_con_asiento_reservado, 1,2)
        self.assertEqual(c, False)
        self.assertEqual (fn.remover_boleto(Avion_con_asiento_reservado,1,1), True)
    def test_despegar_avion (self):
        self.assertEqual(fn.despegar_avion(), "A155")
        self.assertEqual(fn.despegar_avion(), "B453")
        self.assertEqual(fn.despegar_avion(), "J783")
    def test_agregar_avion_queue(self):
        self.assertEqual(fn.agregar_avion_queue(), "D201")
        self.assertEqual(fn.agregar_avion_queue(), "H312")
        self.assertEqual(fn.agregar_avion_queue(), "P231")
        self.assertEqual(fn.agregar_avion_queue(), "F387")
        self.assertEqual(fn.agregar_avion_queue(), "U476")