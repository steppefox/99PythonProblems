# P23 (**) Extract a given number of randomly selected elements from a list.
# The selected items shall be returned in a list.
# Example:
# * (rnd-select '(a b c d e f g h) 3)
# (E D A)

from random import randrange

def rand_list(arr,count):
	sublist = []
	for i in range(count):
		sublist.append(arr.pop(randrange(len(arr))-1))
	return sublist

arr = ['a','b','c','d','e','f','g','h']
print arr
print rand_list(arr,3)