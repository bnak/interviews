from __future__ import division

'''

def sum_odd_fibs(a,b,limit,sum_of_odds):
	if a > limit or b > limit:
		return sum_of_odds
	else: 
		min(a,b) = a+b
		if max(a,b)% 2 ==1:
			sum_of_odds += (a,b)
		return sum_of_odds(a,b, limit,sum_of_odds)
'''


def sum_odd_fibs2(fibs, limit, sum_of_odds): 
	if not fibs: 
		fibs = [0,1]
		return sum_odd_fibs2(fibs, limit, sum_of_odds)
	elif fibs[-1] < limit:
		if fibs[-1] % 2 ==1: 
			sum_of_odds += fibs[-1]
		fibs.append(fibs[-1] + fibs[-2])
		return sum_odd_fibs2(fibs, limit, sum_of_odds)
	else: 
		return sum_of_odds
		

def fibs(n):
	if n == 0: 
		return 0
	elif n ==1: 
		return 1
	else: 
		return fibs(n-1) + fibs(n-2)

def list_of_fibs (n):
	list1 = []
	for i in range(n): 
		list1.append(fibs(i))
	return list1

def sum_of_odds(list1):
	sum_of_odds = 0
	for item in list1:
		if item%2 == 1: 
			sum_of_odds+= item

	return sum_of_odds

def reverse_string_nip(string1):
	# not in place
	reversed_string=[]
	for char in string1: 
		reversed_string.insert(0, char)

	return "".join(reversed_string)

def reverse_string_recursive(string1):
	if string1 != "": 
		return string1[-1:]+ reverse_string_recursive(string1[:-1])
	else:
		return ""

def reverse_nip(array1):
	array1reverse = []
	if not array1:
		return []
	for i in range(len(array1)): 
		array1reverse.append(array1[-(i+1)])
	return array1reverse

def reverse_array_ip(array1):
	if array1: 
		return array1[-2:-1] + reverse_array_ip(array1[:-1])
	else: 
		return []

def string_to_float(string1):
	math_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
	num = 0
	decimal_place = 0	
	for i in range(len(string1)):
		if string1[i] == '.':
			decimal_place = len(string1)-i-1
			num = num/10
		else:
			if math_dict[string1[i]]:
				num += ((math_dict[string1[i]])*(10**(len(string1)-1-i)))
			else: 
				return "Not valid"

	return num/(10**decimal_place)


def palindrome_checker(string1):
	is_palindrome = True

	i = 0

	while i < (len(string1)/2):
		if string1[i] == string1[-(i+1)]:
			i +=1
		else: 
			i = len(string1)
			is_palindrome = False

	return is_palindrome

""""purpose of inheritance, inner join vs outer join, etc"""

def main():

	#print string_to_float("234.56")
'''

	print sum_odd_fibs2([], 1000, 0)
	print sum_odd_fibs2([], 40, 0)
	print sum_of_odds(list_of_fibs(10))
	print reverse_string_nip('teststring')
	print reverse_string_recursive('teststring')
	print reverse_string_recursive('racecar')
	print reverse_nip([])
	print reverse_nip([0,1,2,3,4,5])
	print reverse_array_ip([])
	print reverse_array_ip(['a','b','c','d','e'])
'''




if __name__ == '__main__':
	main()