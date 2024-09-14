from fractions import *


def fractionate(amount: int):
    numerator = 1
    denominator = amount
    fractionate_list = []

    for i in range(amount):
        fractionate_list.append(Fraction(numerator, denominator))
    
    return fractionate_list


if __name__ == "__main__": 
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))