# P17 (*) Split a list into two parts; the length of the first part is given.
# Do not use any predefined predicates.

# Example:
# * (split '(a b c d e f g h i k) 3)
# ( (A B C) (D E F G H I K))

def split_list(arr,num):
	ret = [[],[]]
	for index in range(len(arr)):
		if (index+1)>num:
			ret[1].append(arr[index])
		else:
			ret[0].append(arr[index])
	return ret



arr = ['a','b','c','d','e','f','g','h','i','k']
print arr
print split_list(arr,3)