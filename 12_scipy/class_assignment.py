import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg, interpolate, optimize, cluster

# problem 1
# solve
# x + 5y + z = 6
# 3x + 7y + 2z = 9
# 5x + 11y + 3z = 12
# expected result: x = -3, y = 0, z = 9
# solution in 3 lines


m = np.array([[1,2],[3,4]])
# problem 2
# get the inverse of matrix m and transpose it and get its determinant
# solution in 3 lines


def f1(x):
    return x**3 + 1

# problem 3
# create as linear interpolation of f1 from ten points from -1 to 1 with added noise
# create 100 points from -1 to 1 and get their interpolated values
# plot the original points as blue markers and a red line for the interpolated curve
# save plot as test_1.png
# solution in 6-7 lines


def f2(x, a, b):
  return a * np.exp(-b / x) + 10

# problem 4
# sample function f2 with 50 evenly spaced points from 0.5 to 10
# add noise
# fit data back to f2 and get values for a and b
# plot orginal data in blue, noisy data in red and fitted data in green
# save plot as test_2.png
# solution in 6-7 lines


a = np.random.multivariate_normal([10, 10], [[3, 1], [1, 4]], size=[100])
b = np.random.multivariate_normal([-5, -5], [[6, 1], [6, 4]], size=[100])
c = np.random.multivariate_normal([0, 0], [[6, 1], [6, 4]], size=[100])
d = np.random.multivariate_normal([-10, 10], [[6, 1], [6, 4]], size=[100])
# problem 5
# pool the data together for a,b,c,d and perform k means clustering with 4 cluster
# assign each point a cluster and plot all clusters with there own color on a scatter plot
# solution in ~20 lines


