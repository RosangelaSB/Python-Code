import sys # built-in module
import matplotlib.pyplot as plt, matplotlib.mlab as mlab # third-party module


import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

#Funcao linear
x = np.linspace(-5,5,1000)
y=x+2
fig, ax = plt.subplots()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Grafico da funcao y=x+2")
plt.grid()
ax.plot(x,y)

plt.show()

#Funcao quadratica
x = np.linspace(-6,6,100)
y=x**2+4*x-2
fig, ax = plt.subplots()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Grafico da funcao " "$y=x^2+2x+1$")
plt.grid()
ax.plot(x,y)

plt.show()

#Funcao logaritma
x = np.linspace(-6,6,100)
y=np.log2(x)
fig, ax = plt.subplots()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Grafico da funcao $log_2(x)$")
plt.grid()
ax.plot(x,y)

plt.show()

import math
#Funcao exponencial
x = np.linspace(-1,6,10000)
y=np.power(2, x) # y=np.exp2(x)
fig, ax = plt.subplots()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Grafico da funcao exponencial")
plt.grid()
ax.plot(x,y)

plt.show()

