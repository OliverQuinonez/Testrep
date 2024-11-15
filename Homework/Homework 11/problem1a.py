import numpy as np
import matplotlib.pyplot as plt

def driver():
    N=100
    a=-5
    b=5
    #
    
    f = lambda s: 1/(1+s**2)

    #print(trap(f,a,b,N))
    print(simpson(f,a,b,N))



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