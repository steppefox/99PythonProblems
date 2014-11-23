# P07 (**) Flatten a nested list structure.

def flatten(seq):
  def reducer(a, b):
    if isinstance(b, list):
      return a + flatten(b)
    return a + [b]
  return reduce(reducer, seq, [])

print flatten([1,2])
print flatten([[1,1],2])
print flatten([1,[2,3]])
print flatten([1,[2,[3,[4,5]]]])