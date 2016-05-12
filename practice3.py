def merge_sort(array): 

	if len(array)>1: 
		mid = len(array)//2
		left_half = array[:mid]
		right_half = array[mid:]
		merge_sort(left_half)
		merge_sort(right_half)

		i = 0
		j = 0
		k = 0

		while i<len(left_half) and j<len(right_half):
			if left_half[i] < right_half[j]:
				array[k] = left_half[i]
				i+=1
			else:
				array[k] = right_half[j]
				j+=1
			k+=1

		while i<len(left_half): 
			array[k] = left_half[i]
			i+=1
			k+=1

		while j<len(right_half):
			array[k] = right_half[j]
			j+=1
			k+=1

		return array

'''
Suppose you have a million integer numbers. 
Return all possible values of a,b and c such that 
a+b+c<=d. 
d will be provided to you. 
ex: if the numbers are 1,2,3,4,5,6,7 
and d=7 
[1,2,3] 
[1,2,4] 

[1,2,3] will be same as [1,3,2] and [3,2,1]... 

follow up: 

Return all such parts that satisfy the above condition if d is not provided.

'''

'''
Local minimum
'''
def localmin(array):
	i = 0

	while array[i]>= array[i+1]:
		i+=1


	minimum_index = i
	minimum = array[minimum_index]


	return minimum

'''
Code for computing a^b and optimize it.

'''

def power(a,b): 
	if b == 0:
		return a
	else: 
		return a * power(a,b-1)


'''
You are given a string which has numbers and letters. Numbers occupy all odd positions and letters even positions. You need to transform this string such that all letters move to front of array, and all numbers at the end. 

The relative order of the letters and numbers needs to be preserved 

I need to do this in O(n) time and O(1) space. 

eg: a1b2c3d4 -> abcd1234 , x3y4z6 -> xyz346 

Please don't submit your answers if it is not fulfilling the time-space complexity requirements.

'''

def process_string(string):
	
	return string



def main(): 

	print localmin([10,9,7,5,6,8])

if __name__ == '__main__': 
	main()