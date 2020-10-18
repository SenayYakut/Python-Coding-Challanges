'''
Create a function named odd_indices() that has one parameter named lst.

The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.
'''
def odd_indices(lst):
      new_lst = []
  i = 1
  for i in range(i, len(lst), 2):
      new_lst.append(lst[i])
  return new_lst




#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))