import numpy as np
from matplotlib import pyplot as plt
import math

#conditions
particles = 100
x_0 = 0 #initial state
steps = 1000

#constructing transition matrix
def tridiag(a, b, c, k1 = -1, k2 = 0, k3 = 1):
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)

a = np.arange(1, particles + 1 ) / particles
b = np.zeros(particles + 1)
c = np.arange(particles, 0, -1) / particles


P = tridiag(a, b, c)
###

### path simulation
def path(steps, P, x_0):
    X = np.zeros(steps + 1, dtype = np.int)
    X[0] = x_0
    for k in range(steps):
        X[k + 1] = np.random.choice(a = range(len(P)),p =  P[X[k],:])
    return X
###

time = np.arange(steps + 1)
X = path(steps, P, x_0)
plt.plot(time, X)
plt.show()
