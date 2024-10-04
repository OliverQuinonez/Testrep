import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from numpy.linalg import norm

def driver():
    x0 = np.array([1,1,1]) #starting guess form problem3b
    tol = 1e-8
    Nmax = 200


    [xstar,ier,n,itterates] = method3a(x0,tol,Nmax)

    print('Approximate solution: ',xstar)
    print('Indication of error: ', ier)
    print('Number of itterations: ', n)
    print('f(xstar)= ',f(xstar))


    err = np.zeros(n) #array of the error at each itteration
    for i in range(n):
        err[i] = itterates[i]



    it = np.arange(1,n+1) #
    plt.plot(it,np.log10(err)) #plotting log of error vs itteration
    plt.xlabel('n')
    plt.ylabel('$log(e_n)$')
    plt.show()




def f(x):
    return (x[0])**2 + 4*(x[1])**2 + 4*(x[2])**2 - 16 #returns f(x,y,z) from problem 3b
 
def delf(x):
    return np.array([2*x[0],8*x[1],8*x[2]]) #returns the gradiaent of f(x,y,z) from problem3b

def method3a(x0,TOL,Nmax):
    n=0 #counter for number of itterations
    itterates = np.zeros(Nmax)
    while (n<Nmax):

        coeff = 1/(delf(x0)[0]**2 + delf(x0)[1]**2 + delf(x0)[2]**2) # d from problem 3 without f

        Jinv = coeff*np.array([[0,0,delf(x0)[0]],
                          [0,0,delf(x0)[1]],
                          [0,0,delf(x0)[2]]]) #matrix equivilant to J inverse (first two column zero because first two collums of F are zero so theyre redundant)
        F = np.array([0,0,f(x0)])
        x1 = x0 - np.matmul(Jinv,F) #itteration step

        itterates[n] = norm(x0-x1) #Array of error for each itterate

        if (norm(x1-x0) < TOL): #if error less than tollerance return that value 

            ier = 0
            xstar = x1
            return [xstar,ier,n,itterates]
        x0 = x1
        n +=1

    ier = 1
    xstar = x1
    return [xstar,ier,n,itterates]



driver()
