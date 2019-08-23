# Lesson 1: How to Python and variable types 

## How to run python 
Option 1: Use the command line interpreter  

```bash
$ python
>>> print(“hello world”) 
“hello world”
>>> # this is a comment, python ignores these
...
>>> exit() # how you leave the interpreter
```

Option 2: execute a script, always have the extension of your script be ".py"

```bash
$ cat test.py
print(“hello world”)
$ python test.py 
hello world
```
## Numbers 
There are two types of numbers: int or integers, cannot store fractional values, and float or floating point numbers can store any number in a huge range. There are max values for both int and floats

General rule to remember, is if one of your numbers is a float the resultant value will also be a float.

```python
# Number examples
num_1 = 1 # int
num_2 = 1.5 # float 
num_3 = 1. # float 
```

Number operations

```python
>>> 2 + 3 # int addition
5

>>> 2. + 3. # float addition 
5.0

>>> 2. + 3 # still float addition since one of the two number is a float
5.0

>>> 2 - 3  # int substraction 
-1 

>>> 2*3.0 # float multiplication
6.0

>>> 5 / 2 # int division, there can be no fractional values in int, thus is rounded down 
2 

>>> 5. / 2. # float division 
2.5 

>>> int(5. / 2.) # can force values to be integers, by putting int() around it 
2 

>>> float(5 / 2) # likewise can force a int into a float 
2.5

>>> 1 == 1 # with ints it is always possible to check to see if they are same value with "==" operator 
True



```


## Strings 

Strings store text or any series of characters

```python
# String examples 
# can use 'single quotes' or "double quotes" or """triple quotes"""
# triple quotes and span multiple lines
str_1 = "Hello World"
str_2 = '100'
str_3 = """sdgwerg@#$@
			 #$%343 """
```
Operations with strings 

```python
>>>"hello" + "world" # concatenation or string addition
'helloworld'

>>>"hello"*3 # repetition or string multiplication
'hellohellohello'

>>>"hello"[0] # indexing, getting a specific character 
'h'

>>>"hello"[-1] # indexing from the end
'o'

>>>"hello"[1:4] # slicing, getting a series of characters or a substring, format is string[start character:end character]
'ell' 

>>>len("hello") # get the length or size 
5 

>>>"hello" < "jello" # comparision, compares each letter at a time, the letter that later in the alphebet is 'larger'
True

>>> "hello" < "j" # j is after h thus "j" is greater then "hello"
True

>>> "hello" < "g" # g is before h so "hello" is greater then "g"
False

>>> "hello" < "h" # if they are the same character it moves to the next character in the comparision or if there are no more the longer string is greater
False

>>> "hello" == "hello" # string equivalence, must be the same case! 
True

>>> "hello" == "Hello" 
False

>>> "e" in "hello" # substring search 
True 

>>> "llo" in "hello" 
True

>>> "elo" in "hello" 
False

```