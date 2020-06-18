import math

def fib(n):
  phi = ((1 + math.sqrt(5)) / 2)
  return round((phi**(n + 2)) / math.sqrt(5))

def fib_even_sum(n):
  total = 0
  for x in range(n):
    if x % 2 == 0:
      total += fib(x)
  return total

def main():
  print(fib_even_sum(3))

if __name__ == "__main__":
  main()