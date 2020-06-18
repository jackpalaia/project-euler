def func(x):
  if len(x) == 1:
    return x[0]
  m = func(x[:-1])
  if (x[len(x) - 1] <= m):
    return x[len(x) - 1]
  else:
    return m

print(func([-5,1,0,6,-7,-11,7,2,3,-11,-5,0,0,1]))