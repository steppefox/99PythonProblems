# P08 (**) Eliminate consecutive duplicates of list elements.

def removeDups(arr):
	ret = []
	cur_let = ''
	for cell in arr:
		if cell!=cur_let:
			ret.append(cell)
			cur_let = cell
	return ret

arr = [1,1,1,1,2,2,2,2,3,4,5,6,6,7,8,'a','a','a','b','b','c','e','d']
print removeDups(arr)