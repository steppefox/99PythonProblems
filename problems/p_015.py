# P15 (**) Replicate the elements of a list a given number of times.
# Example:
# * (repli '(a b c) 3)
# (A A A B B B C C C)

def dup(arr,nums):
	ret = []
	for el in arr:
		for num in range(nums):
			ret.append(el)
	return ret

arr = ['a','b','c']
print arr
print dup(arr,3)