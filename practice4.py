import collections

"""
Use the shortest unique prefix to represent each word in array
Input: ["zebra", "dog", "duck", "dot"]
Output: {zebra: "z", dog: "do", duck: "du:}
"""

def build_tree(array, tree_dictionary = {}):
	if not array: 
		return tree_dictionary
	else: 
		for item in array: 
		prefix_tree_dict[item[0]].append(item)
		if len(prefix_tree_dict[item[0]]) > 1: 
			for word in prefix_tree_dict[item[0]]:
				prefix_tree_dict[item[0:2]].append(item)

	return tree_dictionary

def find_unique_prefix(array):
	prefix_tree_dict = collections.defaultdict(list) #key = prefix, value = list of words that follow that prefix
	shortest_prefix = {} #key = words, value = smallest prefix

	prefix_tree_dict[""] = array

	for item in array: 
		prefix_tree_dict[item[0]].append(item)
		if len(prefix_tree_dict[item[0]]) > 1: 
			for word in prefix_tree_dict[item[0]]:
				prefix_tree_dict[item[0:2]].append(item)




	for item in prefix_tree_dict.iterkeys(): 
		if len(prefix_tree_dict[item]) == 1: 
			shortest_prefix[prefix_tree_dict[item][0]] = item




	print prefix_tree_dict
	return shortest_prefix


def main(): 
	array1 = ["zebra", "dog", "duck", "dot"]
	print find_unique_prefix(array1)

if __name__ == '__main__':
	main()