# Lesson 9: Errors, Error Handling and Unittests

Many of you may of encountered errors when trying to get the class assignments to work.

```python
>>> 10 % 0 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
 
>>> 4 * x 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
  
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
```

All of these things python is not sure how to proceed and tells you the issue. For example `ZeroDivisionError` occurs when you try and divide by 0, `NameError` occurs when you use a variable that has not be assigned etc.

Python gives us a way to deal with these situations when they come up. Its called error handling, and python has specific syntax to deal with it

## Error Handling 

```python
try: # If an error occurs in a try block it will go to the except statement below. 
  f = open("test.txt")
  f.readlines()
  f.close()
except:
  print("tried to read from file test.txt but it does not exist")
```

Pythons mechanism for error handling is the try / except blocks. If an error occurs in the try block it will go to the except block. Note you can also have an else, and finally block but they are not nearly as useful be aware of them though.

The except block can react to only a specific error if desired. For example:

```python
try:
  f = open("test.txt")
  f.readlines()
  f.close()
except FileNotFoundError: # IOError in python 2.7, will only execute wiht FileNotFoundError
  print("tried to read from file test.txt but it does not exist")
except: # all other errors
	print("some other error I was not expecting?")
```

You can have as many except blocks as necessary. 

It is also possible to generate your own error 

```python
x = '10'
if type(x) == int: # checks to see if variable is an int 
  x += 10
else:
  raise TypeError("x needs to be an int") # creates and error 
  
#output 
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
TypeError: x needs to be an int
```



## Defining new Exceptions 

Python comes with a set of quite a few exceptions see full list: https://docs.python.org/3/library/exceptions.html. 

Python also allows the definition of entirely new types of errors. This becomes more useful as programs become larger and require specific arguments.

```python
class EmptyStringException(Exception): # new user defined exception
  pass

def concat_string(s1, s2):
  if len(s1) == 0 or len(s2) == 0:
    raise EmptyStringException # raises new exception type
  
  return s1 + s2

print("this is a ", "test")

print("this is a ", "") # raises error

this is a test
Traceback (most recent call last):
  File "test.py", line 12, in <module>
    print(concat_string("this is a", ""))
  File "test.py", line 6, in concat_string
    raise EmptyStringException # raises new exception type
__main__.EmptyStringException
```



## Unittesting 

Unittests are small tests that are designed to make sure each function is working properly. Ideally every function should be tested. Testing also includes making sure errors are activated correctly. Python has its own unittesting framework that you can get by `import unittest`.



To use the unittest framework, one creates a new class that inherits from `unitest.TestCase`. Each test is a function within your new class that begins with `test` 



```python
import unittest

def int_divide(x, y):
  if type(x) != int or type(y) != int:
    raise TypeError("x and y need to be ints")
  if y == 0:
    raise RuntimeError("y cannot be 0")
  
  return x / y

# new class for testing int_divide function
class IntDivideUnittest(unittest.TestCase):
  # testing functions must start with "test" 
  def test_result(self):
    # assertEqual checks that both values are equal to each other
    # expected result is 2, so 2 == 2
    self.assertEqual(int_divide(4, 2), 2)

# automatically runs tests in IntDivideUnittest
unittest.main()

#output
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK


```



We can define more tests, to make sure the errors are working properly.



```python
import unittest

class IntDivideUnittest(unittest.TestCase):
  def test_result(self):
    self.assertEqual(int_divide(4, 2), 2)

  def test_args_are_ints(self):
    # checks to see if the assert TypeError is activated
    with self.assertRaises(TypeError):
      int_divide(4, '2')
      
    with self.assertRaises(TypeError):
      int_divide('2', 4)
  
  def test_divide_by_zero(self):
    # this should raise RuntimeError
    with self.assertRaises(RuntimeError):
      int_divide(4, 0)

    # this is fine
    int_divide(0, 4)
    
# automatically runs tests in IntDivideUnittest
unittest.main()

#output
.
----------------------------------------------------------------------
Ran 3 test in 0.000s

OK



```













