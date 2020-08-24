import numpy as np
from matplotlib import pyplot as plt
import math
import random

particles = 1000000
state_0 = 0
steps = 1000000

state = np.zeros(steps + 1)
state[0] = state_0
for k in range(steps):
    p = state[k] / particles
    state[k + 1] = state[k] + np.random.choice(a = [- 1, +1],p =  [p, 1 - p])

time = np.arange(steps + 1)
plt.plot(time, state)
plt.show()

