# Lesson 1: Basics Part 3


# Functions
functions are one of the cornerstones of programming, basically they are small reusable pieces of code.

```python
# function definition, this tells python what will happen WHEN you call the function.
def function_name(arguments):
	function statements ....
	
#calling a function
function_name(arguments)
```

function examples

```python
def times(x, y): # x and y are both arguments to the function times
	return x * y # the value that is returned when the function is called
	
print(times(2, 4))
#output 
#8

x = times(3, 4) # save the result from the function
print(x)
#output 
#12

#functions can have no arguments
def two():
	return 2 
	
print(two())
#output
#2

print(two()*two())
#output
#4

#functions can have no returns 
def print_statement():
	print("I am in a function")
	
x = print_statement()
#output 
#I am in a function

print(x) # prints None, a value only equal to itself
#output
#None 


#functions can have optional arguments 
def times(x, y=2): # y is 2 unless specified 
	return x * y 

print(times(2)) # equalivant to times(2,2)
#output
#4

print(times(2,3)) # overrides the default value of y=2
#output
#6

```

# Commenting and Documentation 
How to write code that you will remember what it does or other people reading it will understand 

## Self documenting code 
The easiest thing to do increase readability is called self documenting code. Writing code that has variable and function names that are indicators of what they store and what they do

```python
my_list = [1, 3, 5, 7] 
# vs 
odd_numbers = [1, 3, 5, 7]


my_dict = { 
	"New York" : "New York City",
	"Nebraska" : "Lincoln",
}
# vs 
capitals_by_state_name = { 
	"New York" : "New York City",
	"Nebraska" : "Lincoln",
}

def a():
	print "hello world"
	
# vs 
def print_hello_world():
	print "hello world"
```

## Good commenting style
We will be following the google style guide for this class

https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings

avoid describing code, it is not useful, see example below.

```python
# returns True if large_num is greater than 5 <- BAD 
if large_num > 5:		
	return True
```
comments should add to whats happening not just repeat the code 

```python
# calculate y position using linear line relationship from x position, slope and offset
y = m*x + b 
```

## Doc strings 
Documentation strings are builtin help information for a function, that can be accessed by `.__doc__` for each function 

```python
>>> str.__doc__
"str(object='') -> string\n\nReturn a nice string representation of the object.\nIf the argument is a string, the return value is the same object."
```
It is important that ever function you write has its own doc string. Doc strings go right under the function definition with triple quotes

```python
def add(x, y):
	"""performs simple additions between two integers
	
	Args:
		x: the first integer to be added
		y: the second integer to be added
	
	Returns:
		returns the integer x + y 
	"""
	
	return x + y 
	
# here is also the more complex example given by google 

def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    """

```


```



