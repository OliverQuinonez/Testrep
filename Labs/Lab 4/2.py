# import libraries
import numpy as np
    
def driver():

# test functions 
     f1 = lambda x: (10/(x+4))**(1/2)
# fixed point is alpha1 = 1.4987....


     Nmax = 100
     tol = 1e-10

# test f1 '''
     x0 = 1.5
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('Array of itterates:',xstar)
     print('Number of itterations:', len(xstar))
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)

     compute_order(xstar,1.36523001)
    



# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0

    fixedPointsList = []
    while (count <Nmax):

       fixedPointsList.append(x0)
       count = count +1


       x1 = f(x0)

       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [np.array(fixedPointsList),ier]
       x0 = x1


    xstar = x1
    ier = 1
    return [np.array(fixedPointsList), ier]


def compute_order(x,xstar):

    diff1 = np.abs(x[1::]-xstar)

    diff2 = np.abs(x[0:-1]-xstar)

    fit = np.polyfit(np.log(diff2.flatten()),np.log(diff1.flatten()),1)

    _lambda = np.exp(fit[1])

    alpha = fit[0]

    print(f"lambda is {_lambda}")
    print(f"alpha is {alpha}")

    return fit


    

driver()