import numpy as np
import matplotlib.pyplot as plt
import scipy.special

def driver():

    alpha = 0.138E-6 #perameters from problem1 t = 60*24*3600 #60 days converted to seconds
    T_i = 20
    T_s = -15

    t = 60*24*3600 #60 days converted to seconds

    x = np.linspace(0,2,1000)

    f = lambda x: scipy.special.erf(x/(2*np.sqrt(alpha*t))) + T_s/(T_i-T_s)  #f(x) from part a

    plt.plot(x,f(x))# plot f(x)
    plt.plot(x,np.zeros(len(x))) #plot y=0
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.title('Problem 1a')
    plt.show()
    
    return


    

driver()