


def merge_sort(array): 
	if len(array)>1:
		mid = len(array)//2
		left_half = array[:mid]
		right_half = array[mid:]

		merge_sort(left_half)
		merge_sort(right_half)

		i = 0
		j=0
		k=0

		while i<len(left_half) and j<len(right_half):
			if left_half[i] < right_half[j]:
				array[k] = left_half[i]
				i +=1
			else: 
				array[k] = right_half[j]
				j +=1
			k += 1

		while i < len(left_half):
			array[k] = left_half[i]
			i +=1
			k +=1

		while j < len(right_half):
			array[k] = right_half[j]
			j+=1
			k+=1
	return array


"""Sort and print an array of integers with commas between the numbers.
If there are 3 or more in a row (consecutive integers), print the first and last with a dash (-) between them. Like this:
nums = [13, 8, 6, 7, 5, 1, 20, 9, 10]
you print: "1, 5-10, 13, 20"""


def process_array(array):
	array = merge_sort(array)

	i = 0
	number_adjacent = 0

	while i < len(array)-1:
		j = i

		while array[j] + 1 == array[j+1]:

			number_adjacent += 1
			j+=1
			start_range_index = j - number_adjacent
			end_range_index = j

		if number_adjacent>3:
			i += number_adjacent

		else:
			i +=1


	if number_adjacent >=3: 
		range_string = str(array[start_range_index]) + "-" + str(array[end_range_index])
		array = array[:start_range_index] + [range_string] + array[end_range_index+1:]


	return array





def process_array2(array):
	#doesn't work with multiple ranges because indices change
	array = merge_sort(array)

	i = 0
	number_adjacent = 0
	range_dict = {}

	while i < len(array)-1:
		j = i

		while array[j] + 1 == array[j+1]:

			number_adjacent += 1
			j+=1
			start_range_index = j - number_adjacent
			end_range_index = j

			

		if number_adjacent>3:
			range_dict[start_range_index] = end_range_index
			i += number_adjacent
			number_adjacent = 0

		else:
			i +=1


	for item in range_dict.keys(): 
		range_string = str(array[start_range_index]) + "-" + str(array[end_range_index])
		array = array[:start_range_index] + [range_string] + array[end_range_index+1:]


	return array

'''
Given an arraylist of N integers, 
(1) find a non-empty subset whose sum is a multiple of N. 
(2) find a non-empty subset whose sum is a multiple of 2N. 
Compare the solutions of the two questions.

'''
def isMultiple(N, int1): 
	if N % int1 ==0:
		return True
	else: 
		return False

def findSubsets(array): 
	n = len(array)
	subsets = []



	return subsets

def main():
	nums = [13, 8, 6, 7, 5, 1, 20, 9, 10]
	nums2 = [94, 56, 27, 45, 28, 25, 24, 23, 1, 4, 6, 26, 53, 54, 55, 103]
	nums3 = [12, 5, 3, 2, 4]
	print process_array(nums)
	print process_array(nums2)
	print process_array(nums3)






if __name__ == '__main__':
	main()