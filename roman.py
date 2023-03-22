import unittest

def romanCheck(int):
    check = ''
    while int:
        if int == 1:
            check += "I"
        elif int == 5:
            check += "V"
        elif int == 10:
            check += "X"
    return check;
class testRoman(unittest.TestCase):
    def testUno(self):
        self.assertEqual(romanCheck(1), 'I')
    def testTres(self):
        self.assertEqual(romanCheck(3), "III")


if __name__ == '__main__':
    unittest.main()