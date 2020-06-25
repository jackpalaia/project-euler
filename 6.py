def sum_squares():
  return sum([x**2 for x in range(1, 101)])

def square_sum():
  return sum(range(1, 101))**2

def main():
  print(square_sum() - sum_squares())

if __name__ == "__main__":
  main()