import numpy as np
import matplotlib.pyplot as plt
import math
from math import pi

def driver():

    R = 1.2 #Values from the first part of the problem
    dr=0.1
    f=15
    p=0

    theta = np.linspace(0,2*math.pi,1000) #creates a vector for the interval (0,2pi) with 1000 points

    plt.plot(x(R,theta,dr,f,p),y(R,theta,dr,f,p)) #plots the parametric cruve from the first part of the problem
    plt.show()

    dr=0.05 #value for second part of the problem

    for i in range(10):

        R=i #values for second part of the problem
        f=2+i
        p= np.random.uniform(0,2) #randomly distribues p between 0 and 2

        plt.plot(x(R,theta,dr,f,p),y(R,theta,dr,f,p))

    plt.show()

    return

def x(R,theta,dr,f,p): #defines a parametric function x of perameter theta
    return R*(1+dr*np.sin(f*theta+p))*np.cos(theta)

def y(R,theta,dr,f,p): #defines a parametric function y of perameter theta
    return R*(1+dr*np.sin(f*theta+p))*np.sin(theta)


driver()