# P20 (*) Remove the K'th element from a list.
# Example:
# * (remove-at '(a b c d) 2)
# (A C D)

def rem(arr,index):
	arr.pop(index-1)
	return arr

arr = ['a','b','c','d']
print arr
print rem(arr,2), 2