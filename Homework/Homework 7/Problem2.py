import numpy as np 
import matplotlib.pyplot as plt
from numpy.linalg import inv

def driver():
    f = lambda x: 1/(1+(10*x)**2) #function from problem 1
    # N = 20

    # xdata = np.zeros(N)
    # h= 2/(N-1) #formula for h form problem1

    # for i in range(1,len(xdata)+1):
    #     xdata[i-1] = -1 + (i-1)*h #xdata given by formula for x_i from problem1

    # ydata = f(xdata)
    # plt.plot(xdata,ydata,'o')# Plots data with circle markers

    # x = np.linspace(-1,1,1001)

    # interp = eval_Bary_Lagrange(x,xdata,ydata,N)
    # plt.plot(x,interp)
    N = [2,3,4,8,17]
    for Nval in N:

        xdata = np.zeros(Nval)
        h= 2/(Nval-1) #formula for h form problem1

        for i in range(1,len(xdata)+1):
            xdata[i-1] = -1 + (i-1)*h #xdata given by formula for x_i from problem1

        ydata = f(xdata)
        plt.plot(xdata,ydata,'o')# Plots data with circle markers

        x = np.linspace(-1,1,1001)

        interp = eval_Bary_Lagrange(x,xdata,ydata,Nval)
        plt.plot(x,interp)

    plt.xlim(-0.4,0.4)
    plt.ylim(-0.2,1.5)
    plt.legend(['N=2 data','N=2 interpolate','N=3 data','N=3 interpolate','N=4 data','N=4 interpolate','N=8 data','N=8 interpolate','N=17 data','N=17 interpolate',])
    plt.show()




def eval_Bary_Lagrange(xeval,xint,yint,N):
    psi = 1
    weights = np.ones(N+1)

    # for count in range(N+1):
    #    for jj in range(N+1):
    #        if (jj != count):
    #           lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    for jj in range(N):
        psi = psi*(xeval - xint[jj])

    for count in range(N):
        for jj in range(N):
            if (jj != count):
                weights[count] *= 1/(xint[count]-xint[jj])




    yeval = 0.

    for jj in range(N):
        yeval = yeval + yint[jj]*weights[jj]/(xeval-xint[jj])

    yeval = yeval*psi
    return(yeval)


  
    


driver()