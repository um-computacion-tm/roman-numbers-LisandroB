from to_decimal import romanToDecimal;
import unittest;

class testDecimal(unittest.TestCase):
    def test_3(self):
        self.assertEqual(romanToDecimal("III"), 3)
    def test_8(self):
        self.assertEqual(romanToDecimal("VIII"), 8)
    def test_4(self):
        self.assertEqual(romanToDecimal("IV"), 4)
    def test_1(self):
        self.assertEqual(romanToDecimal("I"), 1);
    def test_2(self):
        self.assertEqual(romanToDecimal("II"), 2)
    def test_19(self):
        self.assertEqual(romanToDecimal("XIX"), 19);
    def test_22(self):
        self.assertEqual(romanToDecimal('XXII'), 22);
    def test_t(self):
        self.assertEqual(romanToDecimal('XXI'), 21);
    def test_c(self):
        self.assertEqual(romanToDecimal('XX'), 20);
    def test_d(self):
        self.assertEqual(romanToDecimal('MCMXCIX'), 1999)

if __name__ == '__main__':
    unittest.main();