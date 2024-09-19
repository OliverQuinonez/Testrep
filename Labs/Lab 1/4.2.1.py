
import numpy as np
import numpy.linalg as la
import math
def driver():
    n = 100
    x = np.linspace(-np.pi,np.pi,n)#defines interval from -pi to pi
    # this is a function handle. You can use it to define
    # functions instead of using a subroutine like you
    # have to in a true low level language.
    4
    f = lambda x: np.sin(x) #implements function sin of x
    g = lambda x: np.cos(x) #implements function cos of x
    y = f(x)
    w = g(x)
    # evaluate the dot product of y and w
    dp = dotProduct(y,w,n) # should be equal to zero
    # print the output
    print('the dot product is : ', dp)
    return

def dotProduct(x,y,n):
    # Computes the dot product of the n x 1 vectors x and y
    dp = 0.
    for j in range(n):
        dp = dp + x[j]*y[j] #computes the drop product itterativley
        
    return dp

driver()