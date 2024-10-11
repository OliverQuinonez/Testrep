import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv 
from numpy.linalg import norm 

def driver():
    tol = 1e-6
    Nmax = 200
    x0 = np.array([0,1,2])
    

    [xstar,ier,its] = Newton(x0,tol,Nmax)
    print('xstar from Newton: ',xstar)
    print('Indication of error from Newton: ',ier)
    print('Number of itterations from newton: ',its)


    [x,g1,ier,its] = SteepestDescent(x0, tol, Nmax)
    print('xstar from Steepest Descent: ',x)
    print('Indication of error from Steepest Descent: ',ier)
    print('g(xstar) ',g1)
    print('Number of itterations from Steepest Descent: ',its)

    [p,ier2,its2] = hybrid(x0,Nmax)
    print('xstar from hybrid: ',p)
    print('Indication of error from hybrid: ',ier2)
    print('Number of itterations from hybrid: ',its2)








    


def evalF(x): 
    F = np.zeros(3)
    
    F[0] = x[0] + np.cos(x[0]*x[1]*x[2])-1
    F[1] = (1-x[0])**(1/4) + x[1] + 0.05*x[2]**2 - 0.15*x[2] - 1
    F[2] = -x[0]**2 - 0.1*x[1]**2 + 0.01*x[1] + x[2] -1
    return F
    
def evalJ(v): 
    (x,y,z)= (v[0],v[1],v[2])

    J = np.array([[1-y*z*np.cos(x*y*z),-x*z*np.sin(x*y*z) , -x*y*np.sin(x*y*z) ], 
                  [-1/(4*(1-x)**(3/4)), 1 ,0.1*z -0.15 ], 
                  [-2*x, -0.2*y + 0.01 , 1]])
    return J

def evalg(x):

    F = evalF(x)
    g = F[0]**2 + F[1]**2 + F[2]**2
    return g

def eval_gradg(x):
    F = evalF(x)
    J = evalJ(x)
    
    gradg = np.transpose(J).dot(F)
    return gradg

def Newton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    for its in range(Nmax):
       J = evalJ(x0)
       Jinv = inv(J)
       F = evalF(x0)
       
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier, its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]

def SteepestDescent(x,tol,Nmax):

    for its in range(Nmax):
        g1 = evalg(x)
        z = eval_gradg(x)
        z0 = norm(z)

        if z0 == 0:
            print("zero gradient")

        z = z/z0
        alpha1 = 0
        alpha3 = 1
        dif_vec = x - alpha3*z
        g3 = evalg(dif_vec)

        while g3>=g1:
            alpha3 = alpha3/2
            dif_vec = x - alpha3*z
            g3 = evalg(dif_vec)
            
        if alpha3<tol:
            print("no likely improvement")
            ier = 0
            return [x,g1,ier,its]
        
        alpha2 = alpha3/2
        dif_vec = x - alpha2*z
        g2 = evalg(dif_vec)

        h1 = (g2 - g1)/alpha2
        h2 = (g3-g2)/(alpha3-alpha2)
        h3 = (h2-h1)/alpha3

        alpha0 = 0.5*(alpha2 - h1/h3)
        dif_vec = x - alpha0*z
        g0 = evalg(dif_vec)

        if g0<=g3:
            alpha = alpha0
            gval = g0

        else:
            alpha = alpha3
            gval =g3

        x = x - alpha*z

        if abs(gval - g1)<tol:
            ier = 0
            return [x,g1,ier,its]

    print('max iterations exceeded')    
    ier = 1        
    return [x,g1,ier,its]

def hybrid(x,Nmax): #hybrid steepest descent followed by newton
    tolSteepestDescent =5e-2
    [xnew,g1,ierSteepestDescent,itsSteepestDescent]= SteepestDescent(x,tolSteepestDescent,Nmax)
    [xstar,ierNewton,itsNewton] = Newton(xnew,5e-4,Nmax)

    ier = ierSteepestDescent*ierNewton
    its = itsSteepestDescent + itsNewton
    print(itsSteepestDescent)
    print(itsNewton)


    return [xstar,ier,its]
    
    

driver()