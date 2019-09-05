# Class assignment 

Write a module `file_io.py` that contains four functions 

```python
def get_file_contents(file_name):
	# 1) create file handler to file_name
	# 2) read all lines in file_name
	# 3) close file handler
	# 4) return lines 
	pass

def get_words_in_file(file_name):
	# 1) calls get_file_contents and saves it in a list
	# 2) iterates through each line of the list 
	# 3) for each line splits line into words using .split()
	# 4) creates new list words = []
	# 5) iterate through each word and .append() it to words
	# 6) return words
	pass

def count_words_in_file(file_name):
	# 1) calls get_words_in_file and saves it to a list
	# 2) return length of list 
	pass 
	
def count_word_instances_in_file(file_name, target_word):
	# 1) calls get_words_in_file and saves it to a list 
	# 2) iterates through each word in list
	# 3) for each word compare it to target_word with '==' 
	# 4) have word_match counter if word == target word add one to counter
	# 5) return word_match counter
	pass 

```

`get_file_contents` takes in a file name and returns a list of strings of each line 
`get_words_in_file` returns a list of all the words in a given file
`count_words_in_file` returns number of words in a given file 
`count_word_instances_in_file` returns number of times a given word appeared in a file

In your assignment python file  

```python 

import file_io 

# print out file contents of text.txt using file_io.get_file_contents
# print out all the words in text.txt using file_io.get_words_in_file
# print out the number of words in using file_io.count_words_in_file
# print out the number of times 'test' appears in text.txt using file_io.count_words_in_file
# print out the number of times 'silly` appears in text.txt using file_io.count_words_in_file

```




