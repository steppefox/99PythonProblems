# P25 (*) Generate a random permutation of the elements of a list.
# Example:
# * (rnd-permu '(a b c d e f))
# (B A D C E F)

# Hint: Use the solution of problem P23.

from random import randrange

def rnd_permu(arr):
	ret = []
	some_range = range(len(arr))
	for i in some_range:
		ret.append(arr.pop(randrange(len(arr))))
	return ret


arr = ['a','b','c','d','e','f']
print arr
print rnd_permu(arr)