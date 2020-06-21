def large_pal():
  maxPal = 0
  for i in range(0, 1000):
    for j in range(0, 1000):
      if (str(i * j) == str(i * j)[::-1] and i * j > maxPal):
        maxPal = i * j
  return maxPal

def main():
  print(large_pal())

if __name__ == "__main__":
  main()