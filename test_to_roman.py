import unittest;
from to_roman import funcion_ok 

class PrimerTest(unittest.TestCase):
    def test_1(self):
        resultado=funcion_ok(1);
        self.assertEqual(resultado, 'I');
    def test_2(self):
        resultado=funcion_ok(2);
        self.assertEqual(resultado, 'II')
    def test_3(self):
        resultado=funcion_ok(3);
        self.assertEqual(resultado, 'III')
    def test_4(self):
        resultado=funcion_ok(4);
        self.assertEqual(resultado, 'IV')
    def test_19(self):
        resultado=funcion_ok(19);
        self.assertEqual(resultado, 'XIX');
    def test_22(self):
        resultado=funcion_ok(22);
        self.assertEqual(resultado, 'XXII');
    def test_t(self):
        resultado=funcion_ok(21);
        self.assertEqual(resultado, 'XXI');
    def test_c(self):
        resultado=funcion_ok(20);
        self.assertEqual(resultado, 'XX');
if __name__ == '__main__':
    unittest.main();