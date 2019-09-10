def get_file_contents(file_name):
	"""
	returns all the lines of a text file as a list

	Args:
		file_name: the path of file

	Returns:
		a list of all the lines in the file
	"""

	f = open(file_name)
	lines = f.readlines()
	f.close()
	return lines

def get_words_in_file(file_name):
	"""
	returns a list of all the words in a text file

	Args:
		file_name: the path of file

	Returns:
		a list of all words in the file
	"""

	lines = get_file_contents(file_name)
	all_words = []
	for line in lines:
		# remove lines that don't have words on them
		if len(line) < 2:
			continue
		line = line.rstrip() # removes \n at the end of each line
		words = line.split()
		for word in words:
			all_words.append(word)

	return all_words

def count_words_in_file(file_name):
	"""
	returns the count of all the words in a text file

	Args:
		file_name: the path of file

	Returns:
		the count of all the words in the file (int)
	"""

	return len(get_words_in_file(file_name))

	
def count_word_instances_in_file(file_name, target_word):
	"""
	returns the number of instances of a specific word in a text file

	Args:
		file_name: the path of file
		target_word: the string of a specific word

	Returns:
		the count of all the instances of the target_word in the file
	"""

	count = 0
	words = get_words_in_file(file_name)
	for word in words:
		if target_word == word:
			count += 1
	return count