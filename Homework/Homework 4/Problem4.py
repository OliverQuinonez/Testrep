import numpy as np
import matplotlib.pyplot as plt

def driver():
    x = np.linspace(3,5,1000)
    f = lambda x: np.exp(3*x) - 27*x**6 + 27*x**4*np.exp(x)-9*x**2*np.exp(2*x) #function from prob 4
    fp = lambda x: 3*np.exp(3*x) -162*x**5 + (108*x**3 + 27*x**4)*np.exp(x) -18*(x+x**2)*np.exp(2*x)
    fpp = lambda x: 9*np.exp(3*x) -810*x**4 + (324*x**2+216*x**3+27*x**4)*np.exp(x) - 18*(1+4*x+2*x**2)*np.exp(2*x)

    p0= 3.5
    tol = 10e-7
    Nmax = 100

    m=3 # multiplicity guess for method from problem 2

    # [p,pstar,info,it] = newton(f,fp,p0,tol,Nmax) #regular newton method
    #[p,pstar,info,it] = newtonClass(f,fp,fpp,p0,tol,Nmax) #Modified newton method form class
    [p,pstar,info,it] = newtonProb2(f,fp,m,p0,tol,Nmax)



    print('the approximate root is', '%16.16e' % pstar)
    print('the error message reads:', '%d' % info)
    print('Number of iterations:', '%d' % it)






    


    # plt.plot(x,f(x))
    # plt.plot(x,np.zeros(len(x)))
    # plt.show()

def newtonProb2(f,fp,m,p0,tol,Nmax):
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
      p1 = p0-m*f(p0)/fp(p0)
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]




def newtonClass(f,fp,fpp,p0,tol,Nmax):
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
  p = np.zeros(Nmax+1)
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-1+f(p0)*fpp(p0)/(fp(p0))**2 # Modified newton method for f/f', details in pdf
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]




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