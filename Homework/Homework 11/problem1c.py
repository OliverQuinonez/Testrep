import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scint

def driver():
    N_s=116
    N_t = 644
    a=-5
    b=5
    #
    
    f = lambda s: 1/(1+s**2)

    print('Trapezoildal w N = 644 :', trap(f,a,b,N_t))
    print('Simpsons w N = 116:', simpson(f,a,b,N_s))

    default_quad = scint.quad(f,a,b,full_output = True)
    minusfour_quad = scint.quad(f,a,b,full_output = True, epsabs = 1e-4)



    print('scipy quad with default err tol value: ',default_quad[0]) 
    print('scipy quad with with default err tol number of function evaluations: ', default_quad[2]['neval'] )
    print('scipy quad with 10^-4 err tol value: ',minusfour_quad[0]) 
    print('scipy quad with 10^-4  err tol number of function evaluations: ', minusfour_quad[2]['neval'] )



def trap(f,a,b,N):
    x = np.linspace(a,b,N+1)
    h = (b-a)/N

    w = np.full(N+1,2) #initiallized weights for trapezioidal with all 2's
    w[0] = 1 #set first and last weight to 1
    w[-1] = 1
    w = (h/2)*w #mulitply by h/2 to finilize the weights

    return sum(w*f(x))

def simpson(f,a,b,N):
    x = np.linspace(a,b,N+1)
    h = (b-a)/N

    w = np.ones(N+1)
    for j in range(1,len(w)-1): #initialize the weights
        if (j%2 == 0): #if index is even
            w[j] = 2
        else: # if index is dd
            w[j] = 4
    w = h/3 * w

    return(sum(w*f(x)))







driver()