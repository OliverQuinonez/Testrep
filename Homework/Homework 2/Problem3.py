import numpy as np
import math


def driver():

    x = 9.999999995*10**(-10) #value from problem 3c

    print(func(x))
    print(func2(x))

    return

def func(x): #algorithm from 3b
    y= math.exp(x)
    return y-1

def func2(x): #algorithm from 3d
    return x + x**2/2

driver()