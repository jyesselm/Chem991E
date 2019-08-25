# Lesson 1: How to Python and Python Basics Part 1 
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
## Variables 
Variables are placeholders or 'names' for values one uses in a program. Make sure to use good names for your variables. To set a variables use the = sign. The format is ALWAYS variable = value, as the value is always on the right side and the variable name is on the left side of the =.

``` python 
num_1 = 2 # integer or int  
num_2 = 2.5 # floating point or float
str_1 = "hello" # string or list of characters
list_1 = [1, 2] # a list or a series of values, can store both ints, floats or strings or other lists
dict_1 = {"key" : "value} # dictionary relates an unique key to a value
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
>>>2 + 3 # int addition
5

>>>2. + 3. # float addition 
5.0

>>>2. + 3 # still float addition since one of the two number is a float
5.0

>>>2 - 3  # int subtraction 
-1 

>>>2*3.0 # float multiplication
6.0

>>>5 / 2 # int division, there can be no fractional values in int, thus is rounded down 
2 

>>>5. / 2. # float division 
2.5 

>>>int(5. / 2.) # can force values to be integers, by putting int() around it 
2 

>>>float(5 / 2) # likewise can force a int into a float 
2.5

>>>1 == 1 # with ints it is always possible to check to see if they are same value with "==" operator 
True

>>>1 > 2
False

>>>2 >= 2 # greater or equal 
True

>>>a = 5 
>>>a += 5 # same as a = a + 5
>>>print(a)
10

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

>>>"hello"[0] # indexing, getting a specific character, 0 is the first character in the string
'h'

>>>"hello"[-1] # indexing from the end
'o'

>>>"hello"[1:4] # slicing, getting a series of characters or a substring, format is string[start character:end character]
'ell' 

>>>len("hello") # get the length or size 
5 

>>>"hello" < "jello" # comparision, compares each letter at a time, the letter that later in the alphebet is 'larger'
True

>>>"hello" < "j" # j is after h thus "j" is greater then "hello"
True

>>>"hello" < "g" # g is before h so "hello" is greater then "g"
False

>>>"hello" < "h" # if they are the same character it moves to the next character in the comparision or if there are no more the longer string is greater
False

>>>"hello" == "hello" # string equivalence, must be the same case! 
True

>>>"hello" == "Hello" 
False

>>>"e" in "hello" # substring search 
True 

>>>"llo" in "hello" 
True

>>>"elo" in "hello" 
False

>>>"hello".upper() # convert all characters to uppercase
'HELLO'

>>>"HELLO".lower() # convert all characters to lowercase 
'hello'

>>>"hello".count('l') # counts number of characters 
2

>>>"hello".index('h') # finds the first index of the substring
0

```



## Introduction to getting input from users 
Most programs you have used require you to input some data, the simplest way to do this in python is with the `input` function
 
```python
>>>name = input("enter your name: ") # I will enter Joe when prompted
enter your name: Joe
>>>print(name)
Joe
```


## Introduction to control structures and indentation

if statements allow decisions to be made based on the resultant values of conditionals 

```python
>>>if 5 > 2: #5 is greater than 2 so will execute statement within the if statement. Statements within the if statement are tabbed 
...     print("this is always true")
... 
this is always true

>>>if 5 > 2:
...print("wrong")
  File "<stdin>", line 2
    print("wrong")
        ^
IndentationError: expected an indented block

>>>if 5 > 2:
...  print("correct tabbing")

# if statements can be paired with else statements, 
>>>if 2 > 5:
...   print("will not execute")
...else:
...   print("will execute")
...
will execute

# if statements can also include elif statements which are a combination of a if and else statement.
>>>num = 5
>>>if num == 4:
...  print("num is 4")
...elif num == 5:
...  print("num is 5")
...else:
...  print("num is something else")
num is 5

```


















