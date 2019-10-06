## Pandas part I



### How to read and write csv files into pandas dataframes

```python
import pandas as pd 

# reads a csv file into a pandas dataframe 
df = pd.read_csv("animals.csv")

print(df)
#output
      animal  uniq_id  water_need
0   elephant     1001         500
1   elephant     1002         600
2   elephant     1003         550
3      tiger     1004         300
4      tiger     1005         320
5      tiger     1006         330
6      tiger     1007         290
7      tiger     1008         310
8      zebra     1009         200
9      zebra     1010         220
10     zebra     1011         240
11     zebra     1012         230
12     zebra     1013         220
13     zebra     1014         100
14     zebra     1015          80
15      lion     1016         420
16      lion     1017         600
17      lion     1018         500
18      lion     1019         390
19  kangaroo     1020         410
20  kangaroo     1021         430
21  kangaroo     1022         410

#write dataframe, index=False is optional but removes the extra row pandas always adds
df.to_csv("new_csv.csv", index=False)
```

### Basic operations of a dataframe

```python
print(df.head(2)) #prints the first 2 rows
#output 
     animal  uniq_id  water_need
0  elephant     1001         500
1  elephant     1002         600

print(df.tail(4)) # last 4 rows
#output
      animal  uniq_id  water_need
18      lion     1019         390
19  kangaroo     1020         410
20  kangaroo     1021         430
21  kangaroo     1022         410

print(df.info()) # gives basic information about how many rows, column names if what is the type fo data
#output 
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
animal        22 non-null object
uniq_id       22 non-null int64
water_need    22 non-null int64
dtypes: int64(2), object(1)
memory usage: 600.0+ bytes
None

df_summary = df.describe() # gives statistics for each column, creates a new dataframe
print(df_summary)
#output 
           uniq_id  water_need
count    22.000000   22.000000
mean   1011.500000  347.727273
std       6.493587  147.549243
min    1001.000000   80.000000
25%    1006.250000  232.500000
50%    1011.500000  325.000000
75%    1016.750000  427.500000
max    1022.000000  600.000000

print(len(df)) # gives number of rows
#output 
22

print(df.columns) # prints out the columns in the dataframe
```



### Getting specific row or column information

```python
print(df["animal"]) # gets only the animal column  can also do df.animal 
#output 
0     elephant
1     elephant
2     elephant
3        tiger
4        tiger
5        tiger
6        tiger
7        tiger
8        zebra
9        zebra
10       zebra
11       zebra
12       zebra
13       zebra
14       zebra
15        lion
16        lion
17        lion
18        lion
19    kangaroo
20    kangaroo
21    kangaroo
Name: animal, dtype: object
    
print(df.iloc[0]) # prints the first row 
#output 
animal        elephant
uniq_id           1001
water_need         500
Name: 0, dtype: object

print(df.iloc[0]["animal"]) # gets the animal in the first row
# output
elephant

print(df[["animal", "water_need"]]) # get more than one column at a time
# output
      animal  water_need
0   elephant         500
1   elephant         600
2   elephant         550
3      tiger         300
4      tiger         320
5      tiger         330
6      tiger         290
7      tiger         310
8      zebra         200
9      zebra         220
10     zebra         240
11     zebra         230
12     zebra         220
13     zebra         100
14     zebra          80
15      lion         420
16      lion         600
17      lion         500
18      lion         390
19  kangaroo         410
20  kangaroo         430
21  kangaroo         410
    
    
```

### splicing 

```python
#splicing works just like numpy arrays
df_sub = df[0:5] # rows 0 to 4

print(df_sub)
#output 
     animal  uniq_id  water_need
0  elephant     1001         500
1  elephant     1002         600
2  elephant     1003         550
3     tiger     1004         300
4     tiger     1005         320

df_sub_1 = df[::3] # every third row 
print(df_sub_1)
#output 
      animal  uniq_id  water_need
0   elephant     1001         500
3      tiger     1004         300
6      tiger     1007         290
9      zebra     1010         220
12     zebra     1013         220
15      lion     1016         420
18      lion     1019         390
21  kangaroo     1022         410
```

### Getting rows with specific column values

```python
sub_df = df[df.animal == "elephant"] # gets all rows that are elephants
# this dataframe will behave just like the the original one

print(sub_df)
#output
     animal  uniq_id  water_need
0  elephant     1001         500
1  elephant     1002         600
2  elephant     1003         550

sub_df_2 = df[(df.animal == "kangaroo") & (df.water_need == 410)] # you need ()s or this will not work. But this lets you chain two different searches

print(sub_df_2)
#output
19  kangaroo     1020         410
21  kangaroo     1022         410

sub_df_3 = sub_df = df[(df.animal == "kangaroo") | (df.water_need < 400)] # can either be a kangaroo or need less than 400 or both. 
print(sub_df_3)
      animal  uniq_id  water_need
3      tiger     1004         300
4      tiger     1005         320
5      tiger     1006         330
6      tiger     1007         290
7      tiger     1008         310
8      zebra     1009         200
9      zebra     1010         220
10     zebra     1011         240
11     zebra     1012         230
12     zebra     1013         220
13     zebra     1014         100
14     zebra     1015          80
18      lion     1019         390
19  kangaroo     1020         410
20  kangaroo     1021         430
21  kangaroo     1022         410

```

### Sorting 

```python
df_sort = df.sort_values(["water_need"]) # sort by "water_need" column from lowest to highest

print(df_sort)
#output 
14     zebra     1015          80
13     zebra     1014         100
8      zebra     1009         200
9      zebra     1010         220
12     zebra     1013         220
11     zebra     1012         230
10     zebra     1011         240
6      tiger     1007         290
3      tiger     1004         300
7      tiger     1008         310
4      tiger     1005         320
5      tiger     1006         330
18      lion     1019         390
19  kangaroo     1020         410
21  kangaroo     1022         410
15      lion     1016         420
20  kangaroo     1021         430
17      lion     1018         500
0   elephant     1001         500
2   elephant     1003         550
16      lion     1017         600
1   elephant     1002         600

df_sort_2 = df.sort_values(["water_need"], ascending=False) # flips the order 
print(df_sort_2)
#output 
      animal  uniq_id  water_need
1   elephant     1002         600
16      lion     1017         600
2   elephant     1003         550
0   elephant     1001         500
17      lion     1018         500
20  kangaroo     1021         430
15      lion     1016         420
19  kangaroo     1020         410
21  kangaroo     1022         410
18      lion     1019         390
5      tiger     1006         330
4      tiger     1005         320
7      tiger     1008         310
3      tiger     1004         300
6      tiger     1007         290
10     zebra     1011         240
11     zebra     1012         230
9      zebra     1010         220
12     zebra     1013         220
8      zebra     1009         200
13     zebra     1014         100
14     zebra     1015          80

df_sort_3 = df.sort_values(["water_need", "uniq_id"]) # use multiple values to
sort
print(df_sort_3)
#output 
      animal  uniq_id  water_need
14     zebra     1015          80
13     zebra     1014         100
8      zebra     1009         200
9      zebra     1010         220
12     zebra     1013         220
11     zebra     1012         230
10     zebra     1011         240
6      tiger     1007         290
3      tiger     1004         300
7      tiger     1008         310
4      tiger     1005         320
5      tiger     1006         330
18      lion     1019         390
19  kangaroo     1020         410
21  kangaroo     1022         410
15      lion     1016         420
20  kangaroo     1021         430
0   elephant     1001         500
17      lion     1018         500
2   elephant     1003         550
1   elephant     1002         600
16      lion     1017         600


```

