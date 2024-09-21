import numpy as np
import matplotlib.pyplot as plt

def driver():

    a = 4.82 # [a,b] interval given in problem
    b=5.2
    tol = 1e-4

    f = lambda x: (x-5)**9 #Version of f(x) from part a

    g = lambda x: x**9 - 45*x**8 + 900*x**7 - 10500*x**6 + 78750*x**5 - 393750*x**4 + 1312500*x**3 - 2812500*x**2 + 3515625*x - 1953125 # version of f(x) from part b

    x = np.linspace(a,b,100) 
    plt.plot(x,f(x))#plots f(x)
    plt.plot(x,g(x))#plots g(x)
    plt.legend(['$f(x)$','g(x)'])
    plt.show()

    [astar,count,ier] = bisection(g,a,b,tol)

    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('The number of itterations was',count)
    print('f(astar) =', f(astar))
    




    return


    # define routines
def bisection(f,a,b,tol):
    
    # Inputs:
    # f,a,b - function and endpoints of initial interval
    # tol - bisection stops when interval length < tol
    # Returns:
    # astar - approximation of root
    # ier - error message
    # - ier = 1 => Failed
    # - ier = 0 == success
    # first verify there is a root we can find in the interval
    count = 0

    fa = f(a)
    fb = f(b)
    if (fa*fb>0):
        ier = 1
        astar = a
        return [astar, count ,ier]

    # verify end points are not a root
    if (fa == 0):
        astar = a
        ier =0
        return [astar, count,ier]

    if (fb ==0):
        astar = b
        ier = 0
        return [astar, count,ier]


    d = 0.5*(a+b)

    while (abs(d-a)> tol):
        fd = f(d)
        if (fd ==0):
            astar = d
            ier = 0
            return [astar, count,ier]
        if (fa*fd<0):
            b = d
        else:
            a = d
            fa = fd
        d = 0.5*(a+b)
        count = count +1
    # print('abs(d-a) = ', abs(d-a))

    astar = d
    ier = 0
    return [astar, count,ier]


driver()