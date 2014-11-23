# P16 (**) Drop every N'th element from a list.
# Example:
# * (drop '(a b c d e f g h i k) 3)
# (A B D E G H K)

def dropper(arr,num):
	continue_status = True
	cur_index = 0
	arr_index = 0
	while continue_status:
		cur_index += 1
		if cur_index%num == 0 :
			arr.pop(arr_index)
		else:
			arr_index += 1
		if arr_index > (len(arr)-1):
			continue_status = False
	return arr



arr = ['a','b','c','d','e','f','g','h','i','k']
print arr
print dropper(arr,3)