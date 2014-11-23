# P14 (*) Duplicate the elements of a list.
# Example:
# * (dupli '(a b c c d))
# (A A B B C C C C D D)

def dup(arr):
	ret = []
	for el in arr:
		for num in range(2):
			ret.append(el)
	return ret

arr = ['a','b','c','c','d']
print arr
print dup(arr)