import numpy as np
import matplotlib.pyplot as plt

def driver():
    x = np.linspace(0,5,1000)

    fa = lambda x: (x + (x**2/20)-(x**3/3))/(1+(x/20)+(x**3/120))

    fb = lambda x: (x+(x**2/20))/(1+(x/20) + (x**2/6) + (x**3/120)+(x**4/36))

    T = lambda x: x-x**3/6+x**6/720

    plt.plot(x,abs(fa(x)-T(x))x)
    plt.plot(x,abs(fb(x)-T(x)))

    plt.legend(['error problem a','error problem b'])

    plt.show()

driver()