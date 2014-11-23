# P10 (*) Run-length encoding of a list.
# Use the result of problem P09 to implement the so-called run-length encoding data compression method. Consecutive duplicates of elements are encoded as lists (N E) where N is the number of duplicates of the element E.

# Example:
# * (encode '(a a a a b c c a a d e e e e))
# ((4 A) (1 B) (2 C) (2 A) (1 D)(4 E))

def compact(arr):
	ret = []
	curr_let = ''
	curr_index = -1
	for let in arr:
		if let!=curr_let:
			curr_index += 1
			curr_let = let
			ret.append([])
		ret[curr_index].append(let)

	return ret

def encode(arr):
	arr = compact(arr)
	ret = []
	for el in arr:
		ret.append([len(el),el[0]])
	return ret

arr = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e','e']
print arr
print encode(arr)