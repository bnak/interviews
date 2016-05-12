"""1.1 Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?"""

def hasAllUniqueChars(string1):
	#O(n^2)
	charlist[]
	for char in inputString:
		if char in charlist:
			return False
		else:
		charlist.append(char)
	return True

def hasAllUniqueCharNoDS(string1):
	#O(n^2)
	for char in string1:
		foundCount = 0
		for checkChar in string1:
			if char == checkChar:
				foundCount += 1
			if fountCount > 1:
				return False
	return True

"""1.2 Implement a function that reverses a string"""

def reverseStringRecursive(string1):
	if string1 != "":
		return string1[-1:] + reverseStringRecursive(string1[:-1])
	else:
		return ""

"""1.3 Given two a strings, write a function to decide if 
one is a permutation of the other"""

def isPermutation(string1, string2):
	pass





