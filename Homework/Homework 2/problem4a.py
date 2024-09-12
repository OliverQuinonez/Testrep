import numpy as np
import matplotlib.pyplot as plt
import math
from math import pi

def driver():
    
    t = np.linspace(0 , math.pi, int(math.pi/(math.pi/30)+1) ) #creates a vector starting at 0 and ending at pi, with increments of pi/30

    y = np.cos(t)

    print(sum(t,y))


    return

def sum(v1,v2): #function calculates the sum of the entrywise products of two vectors v1 and v2

    if (len(v1) == len(v2)): #checks that the two vectors are the same length
        
        sum = 0 #initializes the value of the sum to zero
        for k in range(len(v1)):
            sum += sum + v1[k]*v2[k] #computes the kth term in the sum

        return sum

    else:
        print('The vectors are different lengths')
        return



    return

driver()