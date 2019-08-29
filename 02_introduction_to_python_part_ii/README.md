# Lesson 1: Basics Part II, lists, dictionaries and loops 

## Lists
A series of elements, initialized with []

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

## Dictionaries 

A series of 'paired' elements, one is a unique key and one is a value. Instead of using indices like in lists to get values you can specify any value for a key. Dictionaries are defined using {} brackets

```python
>>>d = {'key1' : 'value1', 'key2' : 'value2'}
>>>print(d)
{'key2': 'value2', 'key1': 'value1'}

>>>len(d) # get number of items
2 

>>>d['key1'] # get specific value by a key 
'value1'

>>>d['key3'] # error for an invalid key 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'key3'

>>>d['key3'] = 'value3' # add new key/value to dictionary 
>>>d['key3']
'value3'

>>>d['key3'] = 'new_value' # override previous value 

>>>del d['key'] # removes key/value pair from dictionary 

>>>d.keys() # returns a list of keys in the dictionary 
['key2', 'key1']

>>>d.values() # returns a list of values in the dictionary 
['value2', 'value1']

```
## More information on dictionaries
https://www.w3schools.com/python/python_dictionaries.asp 
https://www.geeksforgeeks.org/python-dictionary/


## Reference Semantics 
Applies to lists, dictionaries and custom objects we will cover in future lectures.

```python
>>>a = [1, 2, 3]
>>>b = a	# now b is another reference or 'name' for the same list 
>>>a.append(4)
>>>print(b)
>>>[1, 2, 3, 4]

# to create a new list instead of giving the same list a new name
# any of these will work 
>>> b = a.copy()
>>> b = list(a)
>>> b = a[::]

```


# Loops
Looping is an central part of programming, allowing the same statement to repeated a set number of times 


## For loop 
the for loop is best thought of as a 'foreach' loop, we want to do something to each element in a list, dictionary or string

```python
# the format of a for loop 
for element in list_of_elements:
	print(element) # would print each element once 
	
```

For loop examples 

```python
for x in range(5):
	print(x)
	
#output: 
#0
#1
#2
#3
#4

nums = [0, 5, 8, 9] 
for n in nums:
	# checks to see if n is equal to 0
	if n == 0:
		print("n ="+str(n))

#output:
#n = 0

# can do the same for strings
str = "hello"
for c in str:
	print(c)

#output:
#h
#e
#l
#l
#o

# also works with dictionaries, iterates both the key and value at the same time 
d = { 0 : "value1", 1 : "value2"}
for key, value in d:
	# checks to see if key equal to 0 
	if key == 0:
		print(value)

#output
#value1
```

## While loop
the while loop is a more generalized loop, it continue to repeat until its condition is NOT true

```python

# will continue until count is equal to 5
count = 0
while count < 5:
	count += 1
	print(count)

#output
#1
#2
#3
#4
#5

while True:
	# infinite loop will never end 
	
```

## Break, continue, and loop else
There are a few other keywords that effect loops

### break
```python
# break will exit from a loop once its reached
while True:
	print("looped")
	break # will only loop once since exits here 

#output 	
#looped 

count = 0
while True:
	print(count)
	count += 1
	if count > 1: 
		break	

#output
#0
#1 
#2

while True:
	while True:
		break # will only exit out the of most recent loop, this will still run forever

```

### continue

```python
# continue forces the next iteration of a loop

for i in range(5):
	continue
	print(i) # this is never reached, no output

for i in range(10):
	if i < 8:
		continue
	print(i)

#output 
#8
#9

```

### loop else 

```python
# an else at the end of a loop executes only when the loop has completely finished 

for i in range(5):
	print(i)
else:
	print("finished loop")
	
#output
#0
#1
#2
#3
#4
#finished loop

for i in range(5):
	print(i)
	break # now the else will not execute since this loop did not finish
else:
	print("finished loop")

#output 
#0

```

## More information on loops
https://www.programiz.com/python-programming/for-loop
https://www.programiz.com/python-programming/while-loop
https://www.learnpython.org/en/Loops
https://www.w3schools.com/python/python_for_loops.asp





