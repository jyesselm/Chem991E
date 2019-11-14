import numpy as np

import math
import matplotlib.pyplot as plt

def sdnorm(x, n=2, d=0.0, s=1.0):
    """
    Standard normal pdf (Probability Density Function)
    """
    return np.exp(-(x- d)**2/n)/np.sqrt(2*math.pi*s)

def sdnorm2(x):
    return -sdnorm(x,10,7) - sdnorm(x,5,0,0.5) - sdnorm(x,1,-7)

x = np.linspace(0, 200, 1000)
plt.plot(x, sdnorm(x, d=100, n=5000)*2.5)
plt.show()
exit()


def markov_chain_sampling(start_x, step_size, n_steps, func):
    current = start_x
    vec = []
    vec.append(current)
    # random moves, uniform proposal distribution
    innov = np.random.uniform(-step_size, step_size, n_steps)
    for i in range(1,n_steps):
        next = current + innov[i] #candidate
        current_y = func(current)
        next_y = func(next)
        # always accept if moving to a more favorable position
        if next_y > current_y:
            acceptance_prob = 1
        # if we are going in the wrong direction take the ratio
        else:
            acceptance_prob = next_y / current_y
        dice_roll = np.random.uniform(0, 1)
        # accept the move
        if dice_roll < acceptance_prob:
            current = next
            vec.append(current)
    return vec

def minimization(start_x, step_size, n_steps, func):
    minimum = 1000
    min_x = 100
    current = start_x
    vec1 = []
    vec2 = []
    # random moves, uniform proposal distribution
    innov = np.random.uniform(-step_size, step_size, n_steps)
    for i in range(1, n_steps):
        next = current + innov[i]  # candidate
        current_y = func(current)
        next_y = func(next)
        vec1.append(current)
        vec2.append(current_y)
        # always accept if moving to a more favorable position
        #print(next_y, current_y)
        if next_y < current_y:
            acceptance_prob = 1
        # if we are going in the wrong direction take the ratio
        else:
            acceptance_prob = abs(next_y / current_y)
        dice_roll = np.random.uniform(0, 1)
        # accept the move
        if dice_roll < acceptance_prob:
            current = next
        if minimum > next_y:
            minimum = next_y
            min_x = current
    return minimum, min_x, vec1, vec2

m_y, m_x, vec1, vec2  = minimization(-10, 2.0, 1000, sdnorm2)

#plotting the results:
#theoretical curve
x = np.linspace(-10, 10, 1000)
y = sdnorm2(x)

plt.plot(x,y,'black')
plt.ylabel('Frequency')
plt.xlabel('x')
#plt.plot([m_x], [m_y], 'ro')
plt.plot(vec1, vec2, 'ro')
plt.plot([m_x], [m_y], 'bs')
#plt.ylim([0, 1])
#plt.show()
plt.savefig("imgs/08.png", dpi=600)

