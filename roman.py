import unittest
def funcion_ok(a):
    roman = ''
    if a > 10:
        firstNumber= a - (a%10);
        secondNumber= a%10; 
        for x in range(firstNumber // 10):
            roman+='X';
        for x in range(secondNumber):
            if secondNumber < 4:
                roman+='I';
            elif secondNumber == 4:
                roman+='IV';
                break;
            elif secondNumber == 5:
                roman+='V'
                break;
            elif secondNumber == 6:
                roman+='VI';
                break;
            elif secondNumber == 7:
                roman+='VII';
                break;
            elif secondNumber == 8:
                roman+='VIII';
                break;
            elif secondNumber == 9:
                roman+='IX';
                break;
            elif secondNumber == 10:
                roman+='X';
                break;
    else:
        for x in range(a):
            if a < 4:
                roman+='I';
            elif a == 4:
                roman+='IV';
                break;
            elif a == 5:
                roman+='V'
                break;
            elif a == 6:
                roman+='VI';
                break;
            elif a == 7:
                roman+='VII';
                break;
            elif a == 8:
                roman+='VIII';
                break;
            elif a == 9:
                roman+='IX';
                break;
            elif a == 10:
                roman+='X';
                break;
    return roman;



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