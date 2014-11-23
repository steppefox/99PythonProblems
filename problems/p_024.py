# P24 (*) Lotto: Draw N different random numbers from the set 1..M.
# The selected numbers shall be returned in a list.
# Example:
# * (lotto-select 6 49)
# (23 1 17 33 21 37)

# Hint: Combine the solutions of problems P22 and P23.

from random import randrange

def lotto_select(count,mparam):
	arr = range(1,mparam+1)
	sublist = []
	for i in range(count):
		sublist.append(arr.pop(randrange(len(arr))-1))
	return sublist

print lotto_select(6,49), 6, 49