import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import math

import monte_carlo

def circle(x):
    return np.sqrt(1 - x ** 2)



area, x, y, check = monte_carlo.integrate(0, 6, np.sin, 100000)
print(area*4)

monte_carlo.plot_integration(x, y, check, np.sin, "05.png")
