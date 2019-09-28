## Cook Book

These are reuable peices of code that are handy to know for class assignments 

#### String operations

- [How to get the length of a string](#How-to-get-the-length-of-a-string)
- [How to split strings by delimiter](#How-to-split-strings-by-delimiter)
- [How to remove the new line from a string](#How-to-remove-the-new-line-from-a-string)
- [How to iterate through each character in a string](#How-to-iterate-through-each-character-in-a-string)
- [Splitting each string in a list by a delimiter](#Splitting-each-string-in-a-list-by-a-delimiter)
- [How to convert a string to a float or an int](#How-to-convert-a-string-to-a-float-or-an-int)

#### File I/O

- [Reading every line in a file](#reading-every-line-in-a-file)
- [Writing to a file](#Writing-to-a-file)
- [Writing a list to a file](#Writing-a-list-to-a-file)
- [Checking to see if file exists](#Checking-to-see-if-file-exists)

#### Functions

- [How to define a function and call it ](#How-to-define-a-function-and-call-it)
- [How to do a proper doc string](#How-to-do-a-proper-doc-string)

#### Classes

- [How to create a object with attributes ](#How-to-create-a-object-with-attributes)
- [How to create a object with a method](#How-to-create-a-object-with-a-method)

#### Error handling

- [How to catch any error](#How-to-catch-any-error)
- [How to catch a specific error](#How-to-catch-a-specific-error)
- [How to raise your own error](#How-to-raise-your-own-error)
- [How to reraise an error](#How-to-reraise-an-error)

#### Unittesting 

- [How to make a unittest](#How-to-make-a-unittest )
- [How to check if two values are equal](#How-to-check-if-two-values-are-equal )
- [How to check if an error has been raised](#How-to-check-if-an-error-has-been-raised)


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

### How to remove the new line from a string

```python
s = "hello world\n" # contains a new line at the the end ("\n")

print(s)

#output 
"hello world
"

print(s.rstrip())
```

### How to iterate through each character in a string

```python
s = "hello"

for c in s:
  print(s)
  
#output
#h
#e
#l
#l
#o
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

### How to convert a string to a float or an int

```python
s = "10"
num = int(s) # convert a string to a int

s = "3.14"
num = float(s) # converts a string to a float
```



## File I/O

### Reading every line in a file

```python
f = open("path_to_file")
lines = f.readlines()
f.close()
```

### Writing to a file

```python
f = opne("text.txt", "w") # allows writing to a test.txt
f.write("I am writing to a file\n")
f.close()
```

### Writing a list to a file

```python
my_list = [1, 2, 3, 4, 5]
f = open("test.txt", "w")
for e in my_list:
  f.write(str(e) + " ")
f.close()
```

### Checking to see if file exists

```python
import os

file_path = "test.txt"
if not os.path.isfile(file_path): # checks to see if file exists
  print("file does not exist")
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

### How to do a proper doc string

```python
def add(x, y):
  """adds two numbers together
  
  Args:
  	x: the first number to add
  	y: the second number to add
  
  Returns:
  	returns x+y which is a the sum of both x and y numbers
  """
  return x + y 
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

### How to create a object with a method 

```python
class TwoFloat(object):
  def __init__(self, float_1, float_2):
    # assigns float_1 and float_2 to internal attributes of the same name
    self.float_1 = float_1
    self.float_2 = float_2 
  
  def sum(self):
    return self.float_1 + self.float_2
  
two_floats = TwoFloat(1.00, 3.14)
print(two_floats.sum()) # prints 4.14

```

## Error Handing 

### How to catch any error 

```python
try: # any error that occurs in a try statement will go to the except block
  "10" * 2.2
except:
  print("There was an error ")

#output 
#There was an error
```

### How to catch a specific error

```python
try:
  "10" * 2.2
except TypeError:
  print("There was an error")

#output 
#There was an error

try: 
  "10" * 2.2
except RuntimeError: # this will not run since the error produced is TypeError
  print("There was an error")
  
  
#output 
#Traceback (most recent call last):
#  File "test.py", line 8, in <module>
#    "10" * 2.2
#TypeError: can't multiply sequence by non-int of type 'float'

```

### How to raise your own error 

```python
# if x is required to be an int we can enforce this by raising an error 
# to stop the user from making a mistake 
x = "10"
if type(x) != int:
  raise TypeError("x has to be an int")
  
x += 2
```

### How to reraise an error

```python
# this is how you convert a general error to a specific error related to your program
# if test.txt is critical to your program you want to inform the user of this specific
# issue not return a general error 
try:
  f = open("test.txt")
except: 
  raise IOError("required file: test.txt does not exist")
```



## Unittesting 

### How to make a unittest 

```python
import unittest 

# how to define a unittest
class TestUnittest(unittest.TestCase):
  # each function that starts with "test" is run independently  
  def test_result(self):
    pass
    
# automatically runs tests in 
# MUST BE INCLUDED
unittest.main()
```

### How to check if two values are equal 

```python
import unittest 

class TestUnittest(unittest.TestCase):
  def test_result(self):
    val_1 = 1
    val_2 = 1
    self.assertEqual(val_1, val_2) 
  
unittest.main()

#output
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.000s

class TestUnittest(unittest.TestCase):
  def test_result(self):
    val_1 = 1
    val_2 = 2
    self.assertEqual(val_1, val_2) # now will fail this test 
  
unittest.main()

#output
#F
#======================================================================
#FAIL: test_result (__main__.TestUnittest)
#----------------------------------------------------------------------
#Traceback (most recent call last):
#  File "test.py", line 11, in test_result
#    self.assertEqual(val_1, val_2)  # now will fail this test
#AssertionError: 1 != 2
#
#----------------------------------------------------------------------
#Ran 1 test in 0.000s

```

### How to check if an error has been raised

```python
import unittest 

def func_that_raises_error():
  raise RuntimeError("I always raise an error")
  
class TestUnittest(unittest.TestCase):
  def test_error(self):
    with self.assertRaises(RuntimeError): #this will check to make sure RuntimeError is raised, another error will not work 
      func_that_raises_error()
  
unittest.main()

#output
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.000s
```





















