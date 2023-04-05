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


