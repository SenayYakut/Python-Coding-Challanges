'''
Create a function called divisible_by_ten() that has one parameter named num.

The function should return True if num is divisible by 10, and False otherwise. Consider using modulo (%) to check for divisibility.
'''

# Write your divisible_by_ten function here:
def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False  
# Uncomment these function calls to test your divisible_by_ten function:
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

#Write your function here
def divisible_by_ten(nums):
  counter = 0
  for num in nums:
    if num % 10 == 0:
      counter += 1
  return counter  



#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))