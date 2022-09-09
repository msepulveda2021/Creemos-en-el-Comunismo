"""Copyright (c) 2022 Martin Sepulveda <msepulveda2021@udec.cl>

En este programa resolveremos f(x) = x-exp(-x) == 0
usando el metodo de newton
"""

import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------

def f(x):
	return x - np.exp(-x)

def df(x):
	return 1 + np.exp(-x)

#-------------------------------------------------------------------------------

x = np.linspace(0, 5, 100)

# Metodo de Newton

x_0 = 10 #semilla
x_1 = 1 #semilla1

tolerancia = 1e-5
error = 1.0

while not np.abs(error)>tolerancia:
	error = f(x_0)*(x_1-x_0)/(f(x_1)-f(x_0))
	x_0, x1 = x_1, x_0 - error
	print(x_1)
plt.plot(x_1, f(np.array(x_1)), marker='o')
plt.plot(x, f(x))
plt.show()

