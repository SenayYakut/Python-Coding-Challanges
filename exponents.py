'''
Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.

For example, consider the following code.
'''
def exponents(bases, powers):
      new_lst = []
  for base in bases:
    for power in powers:
      new_lst. append(base ** power)
  return new_lst   



#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

# Solution 2 using lst comprehension
def exponents(bases, powers):
   return [a ** x for a in bases for x in powers]
print(exponents([2, 3, 4], [1, 2, 3]))


