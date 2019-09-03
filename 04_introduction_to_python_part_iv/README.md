# Lesson 1: Basics Part 4, file IO and modules

# Modules 
Modules are 'packages' of code that needs to be grouped together for a specific function or to distribute. Modules are can be loaded with the `import` python keyword

```python
# import the built-in math module 
# math has a lot of common mathematical functions, such as trig functions
>>>import math
>>>math.sin(0) # to access a function or variable in a module you do module_name.function, here we calculate the sin of 0 radians
0.0
>>>math.pi # the value of PI 
3.141592653589793
```

## writing your own module
Here is an short module for testing purposes `mod.py` which you can download in this directory.

```python
# string
test_str = "I am in a module"

# list
test_list = [100, 200, 300]

# function
def add(x, y):
    return x + y 

```
if you download it and use the python interpreter in the same directory you can load it

```python
>>>import mod 
>>>mod.test_str
'I am in a module'

>>>mod.add(10, 20)
30
```

If you are not in the correct directory and you try and load mod 

```python
>>> import mod
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named mod
```

The python interpreter cannot find it, python has a set of directories that it looks for modules to load. You can see this list using the sys module

```python
>>>import sys
>>>sys.path
['', '/Users/jyesselm/Downloads', '/Users/jyesselm/projects/RNAMake', '/Users/jyesselm/projects/RNAMake.projects/SimulateTectos', '/Users/jyesselm/projects/RNAMake.New', '/Users/jyesselm/projects/RNAMake.projects', '/Users/jyesselm/projects/RNAMake.projects/rnamake_server', '/Users/jyesselm/Documents/MATLAB/RDATKit', '/Users/jyesselm/projects', '/Users/jyesselm/projects/RNAMake.tools', '/Users/jyesselm/projects/EteRNABot', '/Users/jyesselm/projects/eternabot_server', '/Users/jyesselm/projects/Rosetta/tools/rna_tools/bin', '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip', '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7', '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin', '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac', '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages', '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk', '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old', '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/readline', '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload', '/Users/jyesselm/Library/Python/2.7/lib/python/site-packages', '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages', '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/gtk-2.0']
```
There are a few ways you can tell python where other python modules are. First add it directly to the sys.path list

```python
>>>import sys
>>>sys.path.append('/Users/jyesselm/projects/Chem991E/04_introduction_to_python_part_iv')
>>>import mod # now I can load the module since python knows where to look
```

Second you can alter the environmental path that python reads, known as `PYTHONPATH`. For Mac and Linux you can add this to your bash file

```bash
# MAC OSX, add a new line in your .bash_profile file in your home directory
# this appends a new directory to the PYTHONPATH list  
# for linux the file is .bashrc
set PYTHONPATH=$PYTHONPATH:/Users/jyesselm/projects/Chem991E/04_introduction_to_python_part_iv

```

For windows its slightly more complicated, here is an article for how to this: https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages/4855685#4855685

## Installing new modules 
One of the other things that have lead to Python's popularity is relative ease to install new modules. There are multiple package managers for python we are going to cover pip but be aware there are others.

For Mac and Linux, pip should already be installed on your system. 

```python
# this will install the numpy package we will be using later, notice we 
# need to put 'sudo' up front which will prompt you for your system
# password. This is because we are changing your system by adding this new package.
$ sudo pip install numpy 
```
Here is an artcicle for how to install pip on windows: https://www.liquidweb.com/kb/install-pip-windows/

You can also install packages through pycharm 

https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html

Which is pretty easy to do.


# File IO

Opening files, writing and reading files. 

In short, the built-in `open` function creates a Python file handler, which serves as a link to a file residing on your machine. After calling `open`, you can transfer strings of data to and from the associated external file by calling the returned file hander's functions.

## Read and writing text files
We are going to use a dummy file given in this directory `test.txt`

```bash
# show the file contents of test.txt
$ cat test.txt 
I am text in a file
I am on the second line
```
Openning a text file to read its contents

```python
# in python 2.7 
for line in open("test.txt"): # open file test.txt for reading
	print line, # print out one line at a time

# in python 3.x 
for line in open("test.txt"):
	print(line, end='')

#output 
I am text in a file
I am on the second line

f = open("test.txt") # open file test.txt for reading 
lines = f.readlines() # read all the lines in the file 
f.close()

print(lines) # lines is list of strings where each element is a line in the file

#output
['I am text in a file\n', 'I am on the second line\n']
```

Openning a file to write 

```python
f = open("test_output.txt", "w") # need to add the "w" argument to write 
f.write("I am writing text to a file\n") # "\n" is a newline character
f.close()
```
check the new file contents

```bash
$ cat test_output.txt 
I am writing text to a file
```

writing lists to files and retrieving the results

```python
numbers = range(10)

# write each number to the file seperated by a " "
f = open("numbers.txt", "w")
for n in numbers:
	f.write(str(n) + " ")
f.close()

# numbers.txt looks like this
0 1 2 3 4 5 6 7 8 9 

numbers_2 = []

# read the first line of number.txt 
f = open("numbers.txt")
number_string = f.readline()
f.close()

# split numbers by " " and put them in numbers_2
for n_str in number_string.split():
	numbers_2.append(int(n_str))

print(numbers_2)

#output 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```

writing dictionaries to files and retrieving the results

```python
mountain_heights = {
	'Mount Everest' : 8848,
	'K2' : 8611,
	'Kangchenjunga' : 8586,
	'Lhotse' : 8516
}

# write each mountain and height seperated by a "," each pair seperated by a newline
f = open("mountains.txt", "w")
for key in mountain_heights:
	f.write(key + "," + str(mountain_heights[key]) + "\n")
f.close()

# mountains.txt looks like this
K2,8611                                                                              
Lhotse,8516                                                                          
Mount Everest,8848                                                                   
Kangchenjunga,8586      

mountain_heights_2 = {}

# read in each line from mountains.txt
f = open("mountains.txt")
lines = f.readlines()
f.close()

# iterate through each line and split line by "," making the first element the key and the second the value
for l in lines:
	spl = l.split(",")
	mountain_heights_2[spl[0]] = int(spl[1])

print(mountain_heights_2)

#output
{'Lhotse': 8516, 'Mount Everest': 8848, 'K2': 8611, 'Kangchenjunga': 8586}

 
```

## Writing python lists and dictionaries directly to files

Now as you can see from above its a real pain to read/write complex pieces of data. Thankfully python supplies a simpler way of reading and writing a list or dictionary directly to a file. 

```python
import pickle # allows direct reading and writing of lists and dictionaries to file 

dict = { 'a' : 0, 'b' : 1, 'c' : 2}
f = open("test.p", "wb") # notice its "wb" not just "w", this is because we are writing in binary not plain text
pickle.dump(dict, f)

# test.p looks like this, its in binary so not readable to humans
<80>^C}q^@(X^A^@^@^@cq^AK^BX^A^@^@^@aq^BK^@X^A^@^@^@bq^CK^Au.   

f = open("test.p", "rb") 
dict_2 = pickle.load(f)

print(dict_2)

#output 
{'c': 2, 'a': 0, 'b': 1}         


```

