# P21 (*) Insert an element at a given position into a list.
# Example:
# * (insert-at 'alfa '(a b c d) 2)
# (A ALFA B C D)

def insert_at(what,where,index):
	where.insert(index-1,what)
	return where

arr = ['a','b','c','d']
print arr
print insert_at('alfa',arr,2), 'alfa', 2