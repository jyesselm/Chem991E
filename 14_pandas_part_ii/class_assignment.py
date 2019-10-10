import pandas as pd
import matplotlib.pyplot as plt

df_imdb = pd.read_csv("IMDB-Movie-Data.csv")

# problem 1
# create new dataframe "df_director" that is a grouping of "Director" from df_imdb with calling
# count see example from class where I used mean instead


#problem 2
# take df_director and create a new data frame df_director_min that contains only the "Director"
# and "Title" columns, in this case "Title" is actually the number of titles the director
# has made based on how we did the grouping earlier


#problem 3
# take df_director_min and sort by "Title" with the highest number first, save it back
# into df_director_min


#problem 4
# take df_director_min and slice the first 30 rows and make a bar plot
# rotate the x-axis 45 degrees plt.xticks(rotation='45')
# save plot to "directors_with_most_movies.png"


# problem 5
# create a dataframe df, df_location, df_sex from csv files: "animals.csv",
# "animal_location.csv", "animal_sex.csv" respectively.
# merge df with df_location and include rows that are shared, i.e. no rows with NaN
# save as df_merge
# merge df_merge with df_sex keep rows regardless of if there is missing data
# save final df into csv file "animals_info.csv"


# problem 6
# create a dataframe in the format of below
# col1 col2 col3
# A    0    1
# B    1    2
# C    2    3
# save it to a csv file