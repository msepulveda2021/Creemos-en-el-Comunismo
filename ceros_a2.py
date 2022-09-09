import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------

x = np.linspace(0, np.pi/2, 100)
y = np.arange(0,1,10)

#-------------------------------------------------------------------------

def u(x,y):
        return np.cos(x) + y*((np.sin(x))**2)

def deriv(f, x, h=1e-3):
        return (f(x+h)-f(x-h))/2*h

#-------------------------------------------------------------------------

for i in range(10):
	u = y[i]
	print(u)

