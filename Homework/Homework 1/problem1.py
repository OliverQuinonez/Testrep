
import numpy as np
import matplotlib.pyplot as plt
import math

def driver():
    x = np.linspace(1.92,2.08,int((2.08-1.92)/0.001)+1) #creates interval of x values with the number of values such that their spacing is 0.001

    plt.plot(x,p(x))#plotting the non-expanded p(x)
    plt.show()

    plt.plot(x,pExp(x))# plotting the expanded p(x)
    plt.show()


    return

def p(x): #gives value p(x) calculated without expanding the binomial
    return (x-2)**9

def pExp(x): #gives value of p(x) calculated by expanding the binomial
    return x**9 -18*x**8 + 144*x**7 - 672*x**6 + 2016*x**5 - 4032*x**4 + 5376*x**3 - 4608*x**2 + 2304*x -512



driver()