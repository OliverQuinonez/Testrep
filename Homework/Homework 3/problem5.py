import numpy as np
import matplotlib.pyplot as plt

def driver():

    x = np.linspace(6.5,7.5,1000)

    f = lambda x: x-4*np.sin(2*x)-3 #function from problem 5

    # plt.plot(x,f(x))
    # plt.plot(x,np.zeros(len(x)))#plotting y=0
    # plt.legend(['f(x)','y=0'])
    # plt.show()

    x0= 2 #root guess, can be changed (and was changed to try to get all 5 roots)
    tol = 1e-11 # error tolerance for 10 correct digits
    Nmax = 100

    [xstar, ier] = fixedpt(f,x0,tol,Nmax)

    print("The root is approximatley:",xstar)
    print('error status:',ier)


    return

def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]


driver()