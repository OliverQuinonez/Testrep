
import numpy as np
import numpy.linalg as la
import math
def driver():
    n = 3
    x = np.array([1,1,1])
    A = np.array([[1,0,0],[0,1,0],[0,0,1]])
    # this is a function handle. You can use it to define
    # functions instead of using a subroutine like you
    # have to in a true low level language.
    4
    f = lambda x: np.sin(x)
    g = lambda x: np.cos(x)
    y = f(x)
    w = g(x)
    # evaluate the dot product of y and w
    p = matrixVectorProduct(A,x,n)
    # print the output
    print('the matrix vector product is : ', p)
    return

def matrixVectorProduct(A,x,n):
    # Computes the dot product of the n x 1 vectors x and y
    p = np.array([0,0,0])
    for i in range(len(p)):
        for j in range(n):
            p[i] = p[i] + A[i][j]*x[j]
    
    return p

driver()