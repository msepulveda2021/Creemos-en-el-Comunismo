"""Copyright (c) 2022 Martin Sepulveda <msepulveda2021@udec.cl>

En este programa resolveremos f(x) = x-exp(-x) == 0
usando el metodo de biseccion
"""

import numpy as np
import matplotlib.pyplot as plt

#---------------------------------------------------------------

def f(x):
	return x - np.exp(-x)

#---Plot-de-la-funcion-------------------------------------------------------------

# crear una lista de valores de x

x = np.linspace(0, 5, 100)
plt.plot(x, f(x)) 
##plt.show()

#---Metodo-de-la-biseccion-------------------------------------------------------------

a = 0
b = 1

for i in range(20):
	c = 0.5*(a+b)

	condicion = f(a)*f(c)

	if condicion < 0:
		b = c
	else:
		a = c

# asumimos que el untimo valor es f(c) = 0
plt.hlines(0.0, 0, 5)
plt.plot(c, f(c), marker = 'o')
plt.show()
