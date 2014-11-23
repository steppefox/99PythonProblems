# P06 (*) Find out whether a list is a palindrome.

def checkPalindrome(st):
	rev_st = st[::-1]
	return rev_st==st

st = 'cookooc'
print checkPalindrome(st)