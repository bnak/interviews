string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):

	word_dict = {}

	words = string1.split()
	
	for item in words: 
		key = item
		word_dict[key] = word_dict.setdefault(key, 0) + 1
		
	return word_dict

def count_unique_list(list1, word_dict):

	for item in list1: 
		key = item
		word_dict[key] = word_dict.setdefault(key, 0) + 1
		
	return word_dict



"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists
"""
'''
def common_items(list1, list2):

	repeat_words = []

	for item in list1:
		for item in list2:
			if item in list1:

'''


"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):


	word_dict = {}

	count_unique_list(list1, word_dict)

	for item in word_dict.keys(): 
		if word_dict[item] > 1:
			word_dict[item] = 1

	count_unique_list(list2, word_dict)

	repeat_words = []

	for item in word_dict.keys(): 
		if word_dict[item] > 1:
			repeat_words.append(item)

	return repeat_words

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):

	pair_sums_to_zero = []

	for i in range(len(list1)-1):
		for j in range(len(list1)):

			if list1[i] + list1[j] == 0:
				pair_sums_to_zero.append((list1[i], list1[j]))

	return pair_sums_to_zero

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
	
	word_dict ={}
	for item in words:
		key = item
		word_dict[key] = word_dict.setdefault(key, 0)+ 1

	return word_dict.keys()

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):

	word_length_dictionary = {}

	for word in words:
		key = word
		word_length_dictionary[key] = word_length_dictionary.setdefault(key, len(word))


	for i in range(max(word_length_dictionary.values())):

		for key in sorted(word_length_dictionary.keys()): 
			if word_length_dictionary[key] == i:
				print key


	return word_length_dictionary

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""
def pirate_translator(): 

	translation = {
		"sir" : "matey",
		'hotel' : 'fleabag inn',
		'student' : 'swabbie',
		'boy' : 'matey',
		'madam' : "proud beauty",
		'professor' : 'foul blaggart',
		'restaurant' : 'galley',
		'your' : 'yer',
		'excuse' : 'arr',
		'students' : 'swabbies',
		'are' : 'be',
		'lawyer' : 'foul blaggart',
		'the' : "th'",
		'restroom' : 'head',
		'my' : 'me',
		'hello' : 'avast',
		'is' : 'be',
		'man' : 'matey'
	}

	sentence = raw_input(">>")
	words_list = sentence.split()
	translated_sentence = []

	for word in words_list:
		if translation.has_key(word):
			translated_sentence.append(translation[word])
		else: 
			translated_sentence.append(word)


	space = ' '
	text_string = space.join(translated_sentence)

	print text_string
