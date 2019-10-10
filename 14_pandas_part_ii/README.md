## Pandas part II

### Other ways to create dataframes

```python
import pandas as pd

# open tab delimited file 
df = pd.read_csv("tab_delim.tsv", sep='\t')
print(df)
#output
     animal  uniq_id  water_need
0  elephant     1001         660
1     zebra     1002         200

df = pd.read_csv("space_delim.txt", sep=' ')
print(df)
#output
     animal  uniq_id  water_need
0  elephant     1001         660
1     zebra     1002         200

# creating a dataframe from a dictionary 
data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
df = pd.DataFrame.from_dict(data)
print(df)
#output 
   col_1 col_2
0      3     a
1      2     b
2      1     c
3      0     d

lst = [['tom', 25], ['krish', 30], 
       ['nick', 26], ['juli', 22]] 
    
df = pd.DataFrame(lst, columns =['Name', 'Age']) 
print(df)
#output 
    Name  Age
0    tom   25
1  krish   30
2   nick   26
3   juli   22


```

 ### Creating a Dataframe from scratch

```python
# creating a new dataframe with 3 columns = [animal, uniq_id, water_need]
df = pd.DataFrame(columns="animal,uniq_id,water_need".split(","))
print(df)
#output 
Empty DataFrame
Columns: [animal, uniq_id, water_need]
Index: []
  
# adding a new row 
df.loc[0] = ["elephant", 1001, 660] # create a new row at position 0 
print(df)
#output 
     animal uniq_id water_need
0  elephant    1001        660

# add another row 
df.loc[1] = ["zebra", 1002, 200] # notice its now loc[1] as this is the second row 
print(df)
#output
     animal  uniq_id  water_need
0  elephant     1001         660
1     zebra     1002         200


```



### Other column operations

```python
import pandas as pd 

df = pd.read_csv("animals.csv")

print(df.animal.unique()) # get all unique row values
print(df["animal"].unique()) # same as above
#output 
['elephant' 'tiger' 'zebra' 'lion' 'kangaroo']

print(df.water_need.mean()) # compute mean for all "water_need" values
#output
347.727272727

print(df.water_need.sum()) # sums all values in "water_need"
#output 
7650

print(df["water_need"].count()) # number of non NaN values
#output
22
```



### Grouping 

```python
# groups together all animals by type and computes the mean
print(df.groupby('animal').mean())
#output
          uniq_id  water_need
animal                       
elephant   1002.0  550.000000
kangaroo   1021.0  416.666667
lion       1017.5  477.500000
tiger      1006.0  310.000000
zebra      1012.0  184.285714

# group by two different values
print(df.groupby(['animal', 'water_need']).mean())
#output
                     uniq_id
animal   water_need         
elephant 500          1001.0
         550          1003.0
         600          1002.0
kangaroo 410          1021.0
         430          1021.0
lion     390          1019.0
         420          1016.0
         500          1018.0
         600          1017.0
tiger    290          1007.0
         300          1004.0
         310          1008.0
         320          1005.0
         330          1006.0
zebra    80           1015.0
         100          1014.0
         200          1009.0
         220          1011.5
         230          1012.0
         240          1011.0
          
# create new dataframe from grouping
new_df = df.groupby('animal', as_index=False).mean() # water_need column is now the average over all animals of that type. 
#output
print(new_df)
     animal  uniq_id  water_need
0  elephant   1002.0  550.000000
1  kangaroo   1021.0  416.666667
2      lion   1017.5  477.500000
3     tiger   1006.0  310.000000
4     zebra   1012.0  184.285714

print(new_df[["animal", "water_need"]]) # selecting only these two columns
#output 
     animal  water_need
0  elephant  550.000000
1  kangaroo  416.666667
2      lion  477.500000
3     tiger  310.000000
4     zebra  184.285714
```



### Merging

```python
df_eats = pd.DataFrame([
  ['elephant','vegetables'], 
  ['tiger','meat'], 
  ['kangaroo','vegetables'], 
  ['zebra','vegetables'], 
  ['giraffe','vegetables']], columns=['animal', 'food'])

print(df_eats)
#output
     animal        food
0  elephant  vegetables
1     tiger        meat
2  kangaroo  vegetables
3     zebra  vegetables
4   giraffe  vegetables

print(df.merge(df_eats)) # merge the two dataframes together into a new dataframe 
# notice there is NO LION, as lion was not included in df_eats and no GIRAFFE as it was not included in df!
# only merges when there is overlap 
#output 
      animal  uniq_id  water_need        food
0   elephant     1001         500  vegetables
1   elephant     1002         600  vegetables
2   elephant     1003         550  vegetables
3      tiger     1004         300        meat
4      tiger     1005         320        meat
5      tiger     1006         330        meat
6      tiger     1007         290        meat
7      tiger     1008         310        meat
8      zebra     1009         200  vegetables
9      zebra     1010         220  vegetables
10     zebra     1011         240  vegetables
11     zebra     1012         230  vegetables
12     zebra     1013         220  vegetables
13     zebra     1014         100  vegetables
14     zebra     1015          80  vegetables
15  kangaroo     1020         410  vegetables
16  kangaroo     1021         430  vegetables
17  kangaroo     1022         410  vegetables

print(df.merge(df_eats, how='outer'))
# now lion and graffe are back but they have missing values set as NaN, if you use the option 'outer' it will create rows for each column even if they are not completely full with data.
#output 
      animal  uniq_id  water_need        food
0   elephant   1001.0       500.0  vegetables
1   elephant   1002.0       600.0  vegetables
2   elephant   1003.0       550.0  vegetables
3      tiger   1004.0       300.0        meat
4      tiger   1005.0       320.0        meat
5      tiger   1006.0       330.0        meat
6      tiger   1007.0       290.0        meat
7      tiger   1008.0       310.0        meat
8      zebra   1009.0       200.0  vegetables
9      zebra   1010.0       220.0  vegetables
10     zebra   1011.0       240.0  vegetables
11     zebra   1012.0       230.0  vegetables
12     zebra   1013.0       220.0  vegetables
13     zebra   1014.0       100.0  vegetables
14     zebra   1015.0        80.0  vegetables
15      lion   1016.0       420.0         NaN
16      lion   1017.0       600.0         NaN
17      lion   1018.0       500.0         NaN
18      lion   1019.0       390.0         NaN
19  kangaroo   1020.0       410.0  vegetables
20  kangaroo   1021.0       430.0  vegetables
21  kangaroo   1022.0       410.0  vegetables
22   giraffe      NaN         NaN  vegetables



```

