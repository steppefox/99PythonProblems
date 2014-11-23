# P13 (**) Run-length encoding of a list (direct solution).
# Implement the so-called run-length encoding data compression method directly.
# I.e. don't explicitly create the sublists containing the duplicates, as in problem P09,
# but only count them.
# As in problem P11, simplify the result list by replacing the singleton lists (1 X) by X.

# Example:
# * (encode-direct '(a a a a b c c a a d e e e e))
# ((4 A) B (2 C) (2 A) D (4 E))

def encode_direct(arr):
	cur_letter = ''
	run_status = True
	cur_index = 0
	arr_index = 0
	step = 0
	while run_status:
		step+=1
		letter = arr[arr_index]
		if letter!=cur_letter:
			cur_letter = letter
			cur_index = arr_index
			arr[cur_index] = [1,arr[cur_index]]
			arr_index+=1
		else:
			arr[cur_index][0]+=1
			arr.pop(arr_index)
		if arr_index>(len(arr)-1):
			run_status = False

	for index in range(len(arr)):
		if arr[index][0]==1:
			arr[index] = arr[index][1]
	return arr


arr = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e','e']
print arr
encode_direct(arr)
print arr