import numpy as np

import monte_carlo

def circle(x):
    return np.sqrt(1 - x ** 2)


area, x, y, check = monte_carlo.integrate(0, 1, circle, 100000)
print(area*4)

monte_carlo.plot_integration(x, y, check, circle, "05.png")
