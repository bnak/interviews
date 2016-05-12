"""Sort and print an array of integers with commas between the numbers.
If there are 3 or more in a row (consecutive integers), print the first and last with a dash (-) between them. Like this:
nums = [13, 8, 6, 7, 5, 1, 20, 9, 10]
you print: "1, 5-10, 13, 20"
"""

def merge_sort(list1):
	#print ("Splitting", list1)
	if len(list1) > 1:
		mid = len(list1)//2
		lefthalf = list1[:mid]
		righthalf = list1[mid:]

		merge_sort(lefthalf)
		merge_sort(righthalf)

		i = 0
		j = 0
		k = 0

		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i] < righthalf[j]:
				list1[k] = lefthalf[i]
				i +=1
			else:
				list1[k] = righthalf[j]
				j +=1
			k = k+1

		while i<len(lefthalf):
			list1[k] = lefthalf[i]
			i +=1
			k +=1

		while j<len(righthalf):
			list1[k] = righthalf[j]
			j +=1
			k +=1
	#print ("Merging", list1)



def sort_cluster_print(array1): 
	"""sort, then recursively find clusters, then print"""
	print array1
	clustered_array = []

	for i in range(len(array1)): 
		if i < len(array1)-2:
			clustered_array.append(array1[i])
		elif array1[i+1] == array1[i]+1 and array1[i+2] == array1[i] + 2:
			j = i+2
			while array1[j] == array1[i] + j:
				j+1
			num_in_cluster = j-i
			i = i + num_in_cluster
			clustered_array.append(array1[i:j])
		else: 
			clustered_array.append(array1[i])

	return clustered_array








def main():
	nums = [13, 8, 6, 7, 5, 1, 20, 9, 10]
	merge_sort(nums)
	print sort_cluster_print(nums)




if __name__ == '__main__':
	main()