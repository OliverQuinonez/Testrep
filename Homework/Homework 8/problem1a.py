import numpy as np
import matplotlib.pyplot as plt

def driver():
    f = lambda x: 1/(1+x**2)

    N = 20
    ''' interval'''
    a = -5
    b = 5
   
   
    ''' create equispaced interpolation nodes'''
    xdata = np.linspace(a,b,N+1)
    
    ''' create interpolation data'''
    ydata = f(xdata)
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yeval_l= np.zeros(Neval+1)

    ''' evaluate lagrange poly '''
    for kk in range(Neval+1):
       yeval_l[kk] = eval_lagrange(xeval[kk],xdata,ydata,N)
          
    ''' create vector with exact values'''
    fex = f(xeval)
       

    plt.figure()    
    plt.plot(xeval,fex,'ro-')
    plt.plot(xeval,yeval_l,'bs--') 
    plt.title('Lagrange N=20')
    plt.legend()

    plt.figure() 
    err_l = abs(yeval_l-fex)
    plt.semilogy(xeval,err_l,'ro--',label='lagrange')
    plt.legend()
    plt.title('Lagrange Err N=20')
    plt.show()







def eval_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
  
    return(yeval)

driver()