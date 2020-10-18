'''
Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.
'''
def larger_sum(lst1, lst2):
      lst1_sum = 0
  lst2_sum = 0
  for a in lst1:
    lst1_sum += a

  for b in lst2:
    lst2_sum += b

  if lst1_sum > lst2_sum:
    return lst1
  elif lst1_sum < lst2_sum:
    return lst2
  else:
    return lst1  
      