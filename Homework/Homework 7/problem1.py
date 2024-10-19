import numpy as np 
import matplotlib.pyplot as plt
from numpy.linalg import inv


def driver():
    f = lambda x: 1/(1+(10*x)**2) #function from problem 1
    
    #N = 5 #Number of data points
    

   





    N = [2,3,4,8,17]
    for Nval in N:

        xdata = np.zeros(Nval)
        h= 2/(Nval-1) #formula for h form problem1

        for i in range(1,len(xdata)+1):
            xdata[i-1] = -1 + (i-1)*h #xdata given by formula for x_i from problem1

        ydata = f(xdata)
        plt.plot(xdata,ydata,'o')# Plots data with circle markers

        x = np.linspace(-1,1,1001)

        interp = monomial_interp(xdata,ydata,x,Nval)
        plt.plot(x,interp)
        
    plt.legend(['N=2 data','N=2 interpolate','N=3 data','N=3 interpolate','N=4 data','N=4 interpolate','N=8 data','N=8 interpolate','N=17 data','N=17 interpolate',])
    plt.show()

def monomial_interp(xdata,ydata,x,N):
    #xdata are interpolating nodes
    #x is a vector of x values to evaluate the interpolate at
    V = np.zeros((len(xdata),len(xdata)))
    for i in range(N):
        V[:,i] = xdata**i

    V_inv = inv(V) 
    c = np.matmul(V_inv,ydata) #finds coefficients by invertin matrix
    
    interp = np.zeros(len(x))
    j=0
    for xval in x: #for all values of x for the interpolant to be computed at

        xeval = np.zeros(N)
        for i in range(N):  #each value of x put into a vector consisting of the powers of that x
            xeval[i] = xval**i
        
        interp[j] = np.dot(xeval,c) #Interpolant computed at each x
        j += 1

    return interp
    







driver()