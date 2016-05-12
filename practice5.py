from itertools import *

"""
Print combinations of strings from list of list of strings

Input: [[quick, slow], [brown, red], [fox, dog]]
Output: All combinations (2^3 = 2*2*2)

"""

def phrase_combinations_2(array): 
	phrase_combinations = []
	number_of_words_in_phrase = len(array)
	number_of_choices_per_word = len(array[0])
	i= 0
	j=0

	while i < number_of_words_in_phrase: 
		while j < number_of_choices_per_word:
			phrase = array[i][j]
			print phrase
			j+=1
		i +=1

	return phrase_combinations

def permutations1(iterable, r=None):
	units = []
	pool = tuple(iterable)
	n = len(pool)
	r = n if r is None else r
	for indices in product(range(n), repeat=r):
		if len(set(indices)) == r:
			unit =  tuple(pool[i] for i in indices)
			units.append(unit)
	return units
        	#yield tuple(pool[i] for i in indices)

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
	pool = tuple(iterable)
	n = len(pool)
	r = n if r is None else r
	if r > n:
		return
	indices = range(n)
	cycles = range(n, n-r, -1)
	yield tuple(pool[i] for i in indices[:r])
	while n:
		for i in reversed(range(r)):
			cycles[i] -= 1
			if cycles[i] == 0:
				indices[i:] = indices[i+1:] + indices[i:i+1]
				cycles[i] = n - i
			else:
				j = cycles[i]
				indices[i], indices[-j] = indices[-j], indices[i]
				yield tuple(pool[i] for i in indices[:r])
				break
		else:
			return


def phrase_combinations(array):
	phrase_combinations = []
	number_of_words_in_phrase = len(array)

	for i in range(len(array[0])): 
		for j in range(len(array[1])):
			for k in range(len(array[2])):
				phrase_combinations.append(array[0][i] +" "+  array[1][j] +" "+ array[2][k])

	return phrase_combinations

def main():
	array = [["quick", "slow"], ["brown", "red"], ["fox", "dog"]]
	print phrase_combinations(array)


if __name__ == "__main__": 
	main()