import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------

x = np.linspace(0, np.pi/2, 100)
y = 0.75
#-------------------------------------------------------------------------

def u(x):
	return np.cos(x) + y*((np.sin(x))**2)

def deriv(f, x, h=1e-3):
	return (f(x+h)-f(x-h))/2*h

#-------------------------------------------------------------------------

derivada = deriv(u, x)

plt.plot(x, derivada, color='red')
plt.show()

