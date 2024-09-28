import numpy as np
import matplotlib.pyplot as plt

def driver():

    x = np.linspace(0,3,1000)
    f = lambda x: x**6 - x - 1 # function from problem 5

    fp = lambda x: 6*x**5 -1 

    x0 = 2
    x1 =1 #second point for secant method
    tol = 1e-6
    Nmax = 100

    X = 1.13472 #real root according to desmos 

    [x,xstar,infoSec,itSec] = secant(f,x0,x1,tol,Nmax) 
    [p,pstar,infoNew,itNew] = newton(f,fp,x0,tol,Nmax)


    print('the approximate root according to the secant method is', '%16.16e' % xstar)
    # print('the error message for the secant method reads:', '%d' % infoSec)
    print('Number of iterations for secant method is:', '%d' % itSec)

    print('the approximate root according to the newton method is', '%16.16e' % pstar)
    # print('the error message for the newton method reads:', '%d' % infoNew)
    print('Number of iterations for newton method is:', '%d' % itNew)

    secantErr = np.zeros(itSec)
    newtonErr = np.zeros(itNew)


    for i in range (0,itSec -1):
        secantErr[i] = abs(x[i]-X)
    

    for i in range(0,itNew -1):
        newtonErr[i] = abs(p[i]-X)

    print(newtonErr)
    print(secantErr)

    fig = plt.figure()
    ax = plt.gca()

    ax.scatter(newtonErr[:-1],newtonErr[1:])
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.title('Newton')
    plt.show()

    fig = plt.figure()
    ax = plt.gca()

    ax.scatter(secantErr[:-1],secantErr[1:])
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.title('Secant')
    plt.show()



def secant(f,x0,x1,tol,Nmax): #secant method algorithm
  if(f(x1)-f(x0)==0):
    info = 1
    xstar = x1
    return

  p = np.zeros(Nmax+1);
  p[0] = x1
  for it in range(Nmax):
      m = (f(x1)-f(x0))/(x1-x0)
      x2 = x1-f(x1)/m
      p[it+1] = x2
      if (abs(x2-x1) < tol):
          xstar = x2
          info = 0
          return [p,xstar,info,it]
      x0 = x1
      x1 = x2

  xstar = x1
  info = 1
  return [p,xstar,info,it]


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

