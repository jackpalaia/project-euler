def sum_multiples(n):
  total = 0
  for x in range(n):
    if (x % 3 == 0 or x % 5 == 0):
      total += x
  return total

print(sum_multiples(1000))