import numpy as np
import matplotlib.pyplot as plt
import scipy.special

def driver():

    alpha = 0.138E-6 #perameters from problem1 t = 60*24*3600 #60 days converted to seconds
    T_i = 20
    T_s = -15

    t = 60*24*3600 #60 days converted to seconds

    x = np.linspace(0,2,1000)

    f = lambda x: scipy.special.erf(x/(2*np.sqrt(alpha*t))) + T_s/(T_i-T_s)  #f(x) from part a
    fp = lambda x: 2/(np.sqrt(np.pi))*np.exp(-x**2/(4*alpha*t)) #derivative of f


    p0 = 2 #Inital guess from part c
    tol = 1e-7
    Nmax = 200

    [p,pstar,info,it] = newton(f,fp,p0,tol,Nmax)
    print('the approximate root is',pstar)
    print('the error message reads:',info)
    print('f(astar) =', f(pstar))
    print('Number of itterations:', it)

    
    return

def newton(f,fp,p0,tol,Nmax):
  """
  Newton iteration.
  
  Inputs:
    f,fp - function and derivative
    p0   - initial guess for root
    tol  - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
  Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
     
  """
  p = np.zeros(Nmax+1);
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]


driver()