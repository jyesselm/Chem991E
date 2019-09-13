import file_io

# print out file contents of text.txt using file_io.get_file_contents
print(file_io.get_file_contents("text.txt"))
# print out all the words in text.txt using file_io.get_words_in_file
print(file_io.get_words_in_file("text.txt"))
# print out the number of words in using file_io.count_words_in_file
print(file_io.count_words_in_file("text.txt"))
# print out the number of times 'test' appears in text.txt using file_io.count_words_in_file
print(file_io.count_word_instances_in_file("text.txt", 'test'))
# print out the number of times 'silly` appears in text.txt using file_io.count_words_in_file
print(file_io.count_word_instances_in_file("text.txt", 'silly'))

