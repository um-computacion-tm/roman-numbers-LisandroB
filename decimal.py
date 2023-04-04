import unittest;

def romanToDecimal(f):
    romanDict = {'I': 1, 'V': 5,'X': 10, 'L': 50,'C': 100, 'D': 500,'M': 1000}
    romanBackwards = list(reversed(list(f)))  
    final = 0
    rightValue = romanDict[romanBackwards[0]]  
    for x in romanBackwards:
        leftValue = romanDict[x]
        if leftValue < rightValue:
           final -= leftValue
        else:
            final += leftValue
        rightValue = leftValue
    return final


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