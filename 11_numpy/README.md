# Numpy: or Numerical Python

Numpy implements a lot of fast mathematical operations that would be too slow to do in normal python. Also a lot of the packages we will discuss in the next few lectures are based on numpy 



## Numpy arrays

Arrays are like python lists but are built to only do mathematical operations



```python
# always import as such 
import numpy as np

nums = np.array([2, 3, 4, 5, 6]) # creates a new array 
print(nums) 

#outputs 
#[2, 3, 4, 5, 6]
```



Comparision to lists. Here we look at an example of multiplying both a list and array by 2. With a list you get the strange results of creating a new list with all values twice. While with a numpy array you get maybe a more expected result of multipying every element by 2.



```python
import numpy as np

list_nums = [2, 3, 4, 5, 6]
nums = np.array([2, 3, 4, 5, 6])

print(list_nums * 2) # creates a new list with two copies of the same list in a row
#outputs
#[2, 3, 4, 5, 6, 2, 3, 4, 5, 6]

print(nums * 2) # multiplies every number by two which actually makes sense!
#outputs 
#[ 4  6  8 10 12]

# indexing still works the same way as lists
print(nums[0]) # first element
#outputs
2

print(nums[-1]) # last element
#outputs
6

print(nums[1:3]) # second and third element, returns as a sub array
#outputs
#[2 3]

print(nums[::2]) # gets every other element
#outputs
#[2 4 6]

print(nums[1:4:2]) # gets every other element between position 1 and 4
#outputs
#[3 5]

print(nums[::-1]) # reverses the array
#outputs
#[6 5 4 3 2]

```



If you remember our Vector3 class and how nice to be able to add vectors together easily. Well numpy arrays has this seem functionality

```python
array_1 = np.array([1, 2, 3])
array_2 = np.array([9, 8, 7])

# works for all operations(+,-,/,*)
print(array_1 + array_2) #output [10 10 10]

print(array_1 * array_2) #output [9 16 21]

# compute dot product
print(np.dot(array_1, array_2)) #output 46

# numpy also has a host of other functions that can performed on all numpy arrays
# such as 
# computes the mean of elements in the array
np.mean(array_1) 

# computes the standard deviation of elements in the array
np.std(array_1)

# computes the variance of the elements in the array
np.var(array_1)

```



## Multi dimensional arrays

Arrays can have more then one dimension, allowing for matrix operations 

```python
matrix_1 = np.array([[1, 0, 0], 
                     [0, 1, 0], 
                     [0, 0, 1]]) # identity matrix

matrix_2 = np.array([[1, 1, 1], 
                     [1, 1, 1], 
                     [1, 1, 1]]) 
print(matrix_1)
#outputs
#[[1 0 0]
# [0 1 0]
# [0 0 1]]

# all the same operations work such as (+,-,/,*)
print(matrix_1 + matrix_2)
#outputs
#[[2 1 1]
# [1 2 1]
# [1 1 2]]

# it is also possible to do matrix multiplication
# anything multipled against indentity matrix is always itself
print(np.dot(matrix_1, matrix_2))
#outputs
#[[1 1 1]
# [1 1 1]
# [1 0 1]]

# when working with multidimensional arrays it can be useful to check the shape or the dimensions
print(matrix_1.shape) # reports that the matrix is a 3 by 3 array
#output 
#(3,3) 

# it is also possible to create arrays with even more dimensions
d3_array = np.array([[[1, 1],[1,1]],[[1, 1],[1,1]]])
print(d3_array)
#output
#[[[1 1]
#  [1 1]]
#
# [[1 1]
#  [1 1]]]

print(d3_array.shape)
#output
#(2, 2, 2)
```



### How does splicing work in multidimensional arrays 

```python
matrix_1 = np.array([[1, 2, 3], 
                     [4, 5, 6], 
                     [7, 8, 9]]) 

print(matrix_1[0,0]) # gets the first position in the first row 
#output 
#1

print(matrix_1[:, 0]) # the ":", means all. So if you put it in the first position its all columns
#output
#[1 4 7]

print(matrix_1[0, :]) # gets all elements in the first row
#output
#[1 2 3]

```



## Other useful numpy functions 

```python
# Create an array of ones in a 3 x 4 matrix
np.ones((3,4))
#output 
#[[1. 1. 1. 1.]
# [1. 1. 1. 1.]
# [1. 1. 1. 1.]]

# Create an array of zeros
np.zeros((2,3))
#output
#[[0. 0. 0.]
# [0. 0. 0.]]

# Create an array with random values
np.random.random((2,2))

# Create a full array with value 7
np.full((2,2),7)

# Create an array of evenly-spaced values
np.arange(10,25,5)

# Create an array of evenly-spaced values
np.linspace(0,2,9)
```

