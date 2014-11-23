# P11 (*) Modified run-length encoding.
# Modify the result of problem P10 in such a way that if an element has no duplicates it is simply copied into the result list. Only elements with duplicates are transferred as (N E) lists.

# Example:
# * (encode-modified '(a a a a b c c a a d e e e e))
# ((4 A) B (2 C) (2 A) D (4 E))

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
		if len(el)>1:
			ret.append([len(el),el[0]])
		else:
			ret.append(el[0])
	return ret

arr = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e','e']
print arr
print encode(arr)