# P19 (**) Rotate a list N places to the left.
# Examples:
# * (rotate '(a b c d e f g h) 3)
# (D E F G H A B C)

# * (rotate '(a b c d e f g h) -2)
# (G H A B C D E F)

# Hint: Use the predefined functions length and append, as well as the result of problem P17.

def rotate(arr,index):
	ret = []
	ret = arr[:]
	while index!=0 :
		if index>0 :
			ret.append(ret.pop(0))
			index -= 1
		else :
			ret.insert(0,ret.pop(index))
			index += 1
	return ret


arr = ['a','b','c','d','e','f','g','h']
print arr
print rotate(arr,3), 3
print rotate(arr,-2), -2