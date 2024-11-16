import numpy as np
import matplotlib.pyplot as plt

def driver():
    a = -5
    b= 5
    x = np.linspace(a,b,100)


    f_2 = lambda x: 1/(1+x**2)**2 * (-2+ 8*x**2/(1+x**2))

    f_4 = lambda x: 1/(1+x**2)**3 * (24 + (96*x-144*x**2)/(1+x**2) - 384*x**3/(1+x**2)**2) # the fourth derivative of f(s)

    bound_2 = max(f_2(x))
    bound_4 = max(f_4(x))

    N_s = ( ((bound_4)*(b-a)**5)*10**4/180 )**(1/4)
    N_T = ( (bound_2)*(b-a)**3*10**4/12 )**(1/2)
    print(N_s)
    print(N_T)

 

driver()