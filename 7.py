from math import sqrt

def is_prime(n):
  if n <= 3:
    return n > 1
  elif n % 2 == 0 or n % 3 == 0:
    return False
  
  i = 5
  while i*i <= n:
    if n % i == 0 or n % (1 + 2) == 0:
      return False
    i += 6
  
  return True

def main(n):
  count = 0
  num = 2
  while True:
    if is_prime(num):
      count += 1
      if count == n:
        return num
    num += 1


  

if __name__ == "__main__":
  print(main(10001))