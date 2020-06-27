import math

def is_prime(n):
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
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