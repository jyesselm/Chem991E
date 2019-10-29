import pandas as pd
import matplotlib.pyplot as plt


# problem 1
# create a dataframe df from csv file: "IMDB-Movie-Data.csv"
# solution in 1 line
df = pd.read_csv("IMDB-Movie-Data.csv")

# problem 2
# get number of rows in df dataframe
# solution in 1 line
len(df)


# problem 3
# print out the columns in the data frame
# solution in 1 line
print(df.columns)

# problem 4
# sort the dataframe by "Revenue (Millions)" print out the movie title that made the
# most money
# solution in 2 lines
df_sort = df.sort_values(["Revenue (Millions)"], ascending=False)
print(df_sort.iloc[0].Title)

# problem 5
# plot "Rating" vs "Revenue (Millions)" and save the plot
# solution in 2 lines
plt.scatter(df["Rating"], df["Revenue (Millions)"])
plt.savefig("rating_vs_revenue.png")


# problem 6
# sort dataframe by Metascore, take top 20 movies and plot each movies Revenue as a bar plot
# with titles on the x-axis, rotate x-axis labels by 45 degrees, with the below command
# plt.xticks(rotation='45')
# solution in 3 lines
df_sort = df.sort_values(["Metascore"], ascending=False)[0:20]
plt.bar(df_sort["Title"], df_sort["Revenue (Millions)"])
plt.xticks(rotation='45')
plt.savefig("movies_vs_revenue.png")
#plt.show()

# problem 7
# create a dataframe df_sub for all movies by director "Ridley Scott"
# count the number of movies he directed in this list, and the average rating of his movies
# solution in 3 lines
df_sub = df[df.Director == "Ridley Scott"]
df_sub["Rating"].mean()

# problem 8
# find the movies that made over 500 million dollars and had a meta score above 90
# save to new csv "top_movies.csv"
# solution in 2 lines
df_sub = df[(df["Revenue (Millions)"] > 500) & (df["Metascore"] > 90)]
df_sub.to_csv("top_movies.csv")