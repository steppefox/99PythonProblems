# P12 (**) Decode a run-length encoded list.
# Given a run-length code list generated as specified in problem P11. Construct its uncompressed version.

def decode(arr):
	ret = []
	for row in arr:
		if isinstance(row,list):
			for index in range(row[0]):
				ret.append(row[1])
		else:
			ret.append(row)
	return ret

arr = [[4,'a'],'b',[2,'c'],[2,'a'],'d',[5,'e']]
print arr
print decode(arr)