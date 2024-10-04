import numpy as np
import matplotlib.pyplot as pls
from numpy.linalg import inv
from numpy.linalg import norm

def driver():

    x0 = np.array([1,1]) #inital guess from 1a

    Nmax = 100
    tol = 1e-7

    [xstar,ier,it] = method1a(x0,tol,Nmax)

    print('The solution according to method1a is: ',xstar)
    print('The indication of error according to method1a is: ',ier)
    print('The number of itterations for method1a is: ',it)

    [pstar,ier,it] = Newton(x0,tol,Nmax)

    print('The solution according to Newton is: ',pstar)
    print('The indication of error according to Newton is: ',ier)
    print('The number of itterations for Newton is: ',it)



    return

def evalF(x): #Function form problem1 evaluated at some x vector 
    F = np.zeros(2)
    F[0] = 3*x[0]**2 - x[1]**2
    F[1] = 3 *x[0]*x[1]**2 - x[0]**3 - 1
    return F


def method1a(x0,tol,Nmax):

    A = np.array([[1/6,1/18], #matrix from problem 1
                   [0,1/6]])
    
    n = 0
    while(n<Nmax): #runs until if statement exits from the loop

        x1 = x0 - np.matmul(A,evalF(x0)) #itteration from part a
        n += 1
        if(np.linalg.norm(x1-x0)<= tol): #If sufficiently close to answer
            ier = 0
            return [x1,ier,n]
        x0 = x1 #

    ier = 1
    return [x1,ier,n]

def evalJ(x): #evaluate the jacobian
    J = np.array([[6*x[0], -2*x[1]],
              [3*(x[1]**2 - x[0]**2), 6*x[0]*x[1]]])
    return J


def Newton(x0,tol,Nmax):
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''
    for its in range(Nmax):
        J = evalJ(x0)
        Jinv = inv(J)
        F = evalF(x0)

        x1 = x0 - np.matmul(Jinv,F)

        if (norm(x1-x0) < tol):
            xstar = x1
            ier =0
            return[xstar, ier, its]
        x0 = x1

    xstar = x1
    ier = 1
    return[xstar,ier,its]


driver()