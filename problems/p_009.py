# P09 (**) Pack consecutive duplicates of list elements into sublists.
# If a list contains repeated elements they should be placed in separate sublists.
#
# Example:
# * (pack '(a a a a b c c a a d e e e e))
# ((A A A A) (B) (C C) (A A) (D) (E E E E))

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

arr = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e','e']
print compact(arr)