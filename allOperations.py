def lots_of_math(a,b,c,d):
      summ=(a+b)
  print(summ)
  sub=(c-d)
  print(sub)
  print(summ * sub)
  return (summ * sub) % a
# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0