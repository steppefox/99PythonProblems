# P18 (**) Extract a slice from a list.
# Given two indices, I and K, the slice is the list containing the elements between the
# I'th and K'th element of the original list (both limits included).
# Start counting the elements with 1.

# Example:
# * (slice '(a b c d e f g h i k) 3 7)
# (C D E F G)

def extract_slice(arr,min,max):
	ret = []
	for index in range(len(arr)):
		if index>=(min-1) and index<=(max-1):
			ret.append(arr[index])
	# shortway: ret = arr[min-1:max]
	return ret

arr = ['a','b','c','d','e','f','g','h','i','j','k']
print arr
print extract_slice(arr,3,7)