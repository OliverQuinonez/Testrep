import numpy as np 

def driver():

    a = 1 # [1,4] is the interval from problem 3
    b=4
    tol = 1e-3 #accuracy from problem 3


    f = lambda x: x**3 +x -4  # function from problem 3

    [astar,count,ier] = bisection(f,a,b,tol)

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