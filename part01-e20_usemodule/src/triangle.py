'''Module containing functions calculating triangle properties'''

__author__ = 'Michal'
__version__ = '1.0'

import math

def hypothenuse(length1, length2):
    '''Returns the hypoteuse of right angled triangle when given lengths of two other sides'''
    return math.sqrt(float(length1) ** 2 + float(length2) ** 2)

def area(side1, side2):
    '''Returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters.''' 
    return 0.5 * float(side1) * float(side2)