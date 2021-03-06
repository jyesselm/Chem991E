# always import all these now
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# this is a pandas dataframe
mpg = sns.load_dataset("mpg")

# problem 1
# plot the distribution of mpg save figure as 01.png


# problem 2
# generate a categorical box plot with x=model_year, y=mpg, save as 02.png


# problem 3
# generate a series of relational plots x=horsepower, y=weight, hue=cylinders, with each
# seperate plot being by model year with a wrap of 6
# save as figure 03.png


# problem 4
# generate a pair plot with a hue of car origin only use columns mpg, cylinders and weight
# save as figure 04.png


# problem 5
# generate categorical violin plot with x=cylinders y=mpg, with the hue being the country of origin
# save as figure 05.png


# problem 6
# plot a relation plot with x="horsepower", y="mpg", with hue by the car origin and
# have the size of each marker be by the weight of the car with marker size going from 40 to 400
# save as figure 06.png


# problem 6
# create a data frame with only cars from the usa
# make a categorical swarm plot with x=model_year, y=horsepower, hue by number of cylinders

