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
