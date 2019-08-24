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

## Lists
Are series of elements, initialized with []

``` python
>>>[] # empty list
[]

>>>len([]) # get the number of elements in a list 
0

>>>a = [99, "hello", ["nested", "list"]] # lists can store any value, even other lists!
>>>print(a) # prints the values of the list that is stored in variable 'a'
[99, 'hello', ['nested', 'list']]

>>>len(a) 
3

>>>a[0] # get the values that is stored in the first element in list 'a', remember indexing always starts at 0 not 1.
99

>>>a[1:3] # slicing or getting a sub list, here is getting the last two elements in list 'a'
['hello', ['nested', 'list']]

>>>a[0] = 98 # set the first element to 98 this overrides its previous value which was 99 
>>> print(a)
[98, 'hello', ['nested', 'list']]

>>>a[1:2] = ["new", "list", "elements"] # can add new elements with splicing, replaced 'hello' with three new elements, 'new', 'list' and 'elements'
>>>print(a)
[0, 'new', 'list', 'elements', ['nested', 'list']]

>>>del a[-1] # remove the last element from list
>>>print(a) 
[0, 'new', 'list', 'elements']

>>>a = [0, 1]
>>>b = [2, 3]
>>>a + b # list addition, joins them together 
[0, 1, 2, 3]

>>>b + a
[2, 3, 0, 1]

>>>a * 3 # list multiplication creates with duplicate elements
[0, 1, 0, 1, 0, 1]

>>>a = range(5) # creates a list with elements 0 to 4
>>>print(a)
[0, 1, 2, 3, 4]

>>>a.append(5) # append adds a element to end of a list 
>>>print(a)
[0, 1, 2, 3, 4, 5]

>>>a.pop() # removes last element for list and returns it
5
>>>print(a)
[0, 1, 2, 3, 4]

>>>a.pop(0) # removes the element at the given index, this will remove the first element
0
>>>print(a)
[1, 2, 3, 4]

>>>a.insert(0, 42) # inserts 42 at the beginning of the list 
>>>print(a)
[42, 1, 2, 3, 4]

>>>a.reverse() # reverses the list
>>>print(a)
[4, 3, 2, 1, 42]

>>>a.sort() # sorts the list, for ints it will put lowest number to highest
>>>print(a)
[1, 2, 3, 4, 42]

```

## More useful information on lists
https://www.w3schools.com/python/python_lists.asp
https://www.geeksforgeeks.org/python-list/


