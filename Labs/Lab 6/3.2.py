import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

def driver():
    x0 = np.array([1,0])
    tol = 1e-10
    Nmax = 200

    [xstar,ier,its] =  LazyNewton(x0,tol,Nmax)
    print(xstar)
    print('Newton: the error message reads:',ier) 
    print('Netwon: number of iterations is:',its)

    minDist = 1e-5
    [xstar,ier,its] = slackerNewton(x0,tol,minDist,Nmax)
    print(xstar)
    print('Slacker Newton: the error message reads:',ier) 
    print('Slacker Netwon: number of iterations is:',its)

    


def evalF(x): 

    F = np.zeros(2)
    
    F[0] = 4*x[0]**2 +x[1]**2 - 4
    F[1] = x[0] + x[1] - np.sin(x[0]-x[1])

    return F

def evalJ(x): 

    
    J = np.array([[ 8*x[0], 2*x[1] ], [ 1-np.cos(x[0]-x[1]), 1+np.cos(x[0]-x[1]) ]])
    return J

def LazyNewton(x0,tol,Nmax):

    ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    J = evalJ(x0)
    Jinv = inv(J)
    for its in range(Nmax):

       F = evalF(x0)
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier,its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]   



def slackerNewton(x0,tol,minDist,Nmax):

    ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    J = evalJ(x0)
    Jinv = inv(J)
    for its in range(Nmax):

       F = evalF(x0)
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier,its]

       if (norm(x1-x0)>minDist): #slacker newton step which recomputes jacobian if distance between itterates is too large
            J = evalJ(x0)
            Jinv = inv(J)

       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]


driver()