
import numpy as np
import numpy.linalg as la
import math
def driver():
    n = 100
    x = np.linspace(0,np.pi,n)
    v = np.array([1,1,1])
    A = np.array([[1,0,0],[0,1,0],[0,0,1]])
    # this is a function handle. You can use it to define
    # functions instead of using a subroutine like you
    # have to in a true low level language.
    4
    f = lambda x: x**2 + 4*x + 2*np.exp(x)
    g = lambda x: 6*x**3 + 2*np.sin(x)
    y = f(x)
    w = g(x)
    # evaluate the dot product of y and w
    dp = np.dot(y,w)
    p = np.matmul(A,v)
    # print the output
    print('the dot product is : ', dp)
    print('the matrix vector product is:', p)
    return

def dotProduct(x,y,n):
    # Computes the dot product of the n x 1 vectors x and y
    dp = 0.
    for j in range(n):
        dp = dp + x[j]*y[j]
        
    return dp

driver()