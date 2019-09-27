## CookBook

These are reuable peices of code that are handy to know

##### string operations

- [Reading every line in a file](# Reading every line in a file)
- [Splitting each string in a list by a delimiter](#Splitting each string in a list by a delimiter)



## String Operations



### How to get the length of a string

```python
s = "hello world"
print(len(s)) # len() gets the length of a string

#output
#11

s = ""
print(len(s)) # empty string has a length of 0

#output 
#0
```



### How to split strings by delimiter

```python
s = "hello world"
print(s.split()) # no argument splits over " "

#output 
#['hello', 'world']

s = "hello,world"
print(s.split()) # creates a list with 1 element, there are no " " in the string

#ouput 
#['hello,world']

print(s.split(",")) # splits over comma

#output
#['hello', 'world']

```



### How to remove the new line from a String

```python
s = "hello world\n" # contains a new line at the the end ("\n")

print(s)

#output 
"hello world
"

print(s.rstrip())
```





### Splitting each string in a list by a delimiter

```python
# split string by spaces
strings = ["hello word", "the quick fox jumped over the lazy dog"]
for string in strings:
  spl = string.split(" ") # splits every line over a space 
	print(spl)
  
#output 
#['hello', 'world']
#['the', 'quick', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']

for string in strings:
  spl = string.split("l") # splits every line over a "l"
  
#output 
#['he', '', 'o word']
#['the quick fox jumped over the ', 'azy dog']
```



### Reading every line in a file

```python
f = open("path_to_file")
lines = f.readlines()
f.close()
```





## Functions 

### How to define a function and call it 

```python
# defining a new function called plus_one that takes one argument
# defining the function DOES NOT CALL IT
def plus_one(arg_1):
  return arg_1 + 1

# calling plus_one function 
print(plus_one(5)) # prints 5 + 1 
```







## Classes

### How to create a object with attributes 

```python
# simple class that holds two different floats
class TwoFloat(object):
  def __init__(self, float_1, float_2):
    # assigns float_1 and float_2 to internal attributes of the same name
    self.float_1 = float_1
    self.float_2 = float_2 
    
two_floats = TwoFloat(1.00, 3.14)
print(two_floats.float_1, two_floats.float_2)

```





### Storage objects

You want to 

```python

```

