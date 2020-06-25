def prime_factors(n):
  factors = []
  temp = n
  x = 2

  while x < n:
    if (temp % x == 0):
      factors.append(x)
      temp /= x
      if (x == 1):
        break
      continue
    x += 1

  if (len(factors) == 0):
    return [n]

  return factors

def divisible():
  factorDict = {}
  for x in range(1, 21):
    tempDict = {}
    factors = prime_factors(x)
    for j in factors:
      if j not in tempDict.keys():
        tempDict[j] = 1
      else:
        tempDict[j] += 1
    for k in tempDict.keys():
      if k not in factorDict.keys():
        factorDict[k] = tempDict[k]
      else:
        if tempDict[k] > factorDict[k]:
          factorDict[k] = tempDict[k]
  print(factorDict)
  product = 1
  for k, v in factorDict.items():
    for _ in range(v):
      product *= k
  return product


def main():
  print(divisible())

if __name__ == "__main__":
  main()