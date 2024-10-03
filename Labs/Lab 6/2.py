import numpy as np
import matplotlib.pyplot as plt

def driver():
    #x = np.linspace(0,np.pi,1000)
    x = np.pi/2
    f = lambda x: np.cos(x)

    h = 0.01*2.**(-np.arange(0,10))

    print(centeredDiff(f,x,h))
    print(forwardDiff(f,x,h))





def forwardDiff(f,x,h):
    return (f(x+h)-f(x))/h

def centeredDiff(f,x,h):
    return (f(x+h)-f(x-h))/2*h




driver()