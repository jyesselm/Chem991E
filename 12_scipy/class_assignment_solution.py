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
equation = np.array([[1, 5, 1], [3, 7, 2], [5, 11, 3]])
solution = np.array([[6], [9], [12]])
roots = linalg.solve(equation, solution)

m = np.array([[1,2],[3,4]])
# problem 2
# get the inverse of matrix m and transpose it and get its determinant
# solution in 3 lines
inv = linalg.inv(m)
t = inv.transpose()
d = linalg.det(t)

def f1(x):
    return x**3 + 1

# problem 3
# create as linear interpolation of f1 from ten points from -1 to 1 with added noise
# create 100 points from -1 to 1 and get their interpolated values
# plot the original points as blue markers and a red line for the interpolated curve
# save plot as test_1.png
# solution in 6-7 lines
x = np.linspace(-1, 1, 10)
noise = (np.random.random(10)*2 - 1) * 1e-1
y = f1(x) + noise

linear_interp = interpolate.interp1d(x, y)

interpolation_points = np.linspace(-1, 1, 1000)
linear_results = linear_interp(interpolation_points)


def f2(x, a, b):
  return a * np.exp(-b / x) + 10

# problem 4
# sample function f2 with 50 evenly spaced points from 0.5 to 10
# add noise
# fit data back to f2 and get values for a and b
# plot orginal data in blue, noisy data in red and fitted data in green
# save plot as test_2.png
# solution in 6-7 lines
x = np.linspace(0.5, 10, 50)
y_org = f2(x, 1.75, 1.5) # actual answer
y_noise = 0.1 * np.random.normal(size=len(x)) # added noise
y = y_org + y_noise

plt.plot(x, y_org) # original data in blue
plt.plot(x, y, 'r') # noisy data in red
plt.show()

a = np.random.multivariate_normal([10, 10], [[3, 1], [1, 4]], size=[100])
b = np.random.multivariate_normal([-5, -5], [[6, 1], [6, 4]], size=[100])
c = np.random.multivariate_normal([0, 0], [[6, 1], [6, 4]], size=[100])
d = np.random.multivariate_normal([-10, 10], [[6, 1], [6, 4]], size=[100])
# problem 5
# pool the data together for a,b,c,d and perform k means clustering with 4 cluster
# assign each point a cluster and plot all clusters with there own color on a scatter plot
# solution in ~20 lines

data = np.concatenate((a, b, c ,d))
centroids,output = cluster.vq.kmeans(data,4) # create two cluster centroids
clx,output = cluster.vq.vq(data,centroids) # clx is cluster indentity of each point

cluster_1 = []
cluster_2 = []
cluster_3 = []
cluster_4 = []
i = 0
for a in clx:
    if a == 0:
        cluster_1.append(data[i])
    elif a == 1:
        cluster_2.append(data[i])
    elif a == 2:
        cluster_3.append(data[i])
    else:
        cluster_4.append(data[i])
    i += 1

cluster_1 = np.array(cluster_1)
cluster_2 = np.array(cluster_2)
cluster_3 = np.array(cluster_3)
cluster_4 = np.array(cluster_4)

plt.scatter(cluster_1[:, 0], cluster_1[:, 1]) # cluster 1 in blue
plt.scatter(cluster_2[:, 0], cluster_2[:, 1]) # cluster 2 in orange
plt.scatter(cluster_3[:, 0], cluster_3[:, 1])
plt.scatter(cluster_4[:, 0], cluster_4[:, 1])
plt.savefig("clusters.png")







