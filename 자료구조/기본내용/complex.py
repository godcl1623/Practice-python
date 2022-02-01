def nums_sum(n):
  total = 0
  for index in range(1, n+1):
    total += index
  print(total)

nums_sum(100)

def sum_nums(n):
    print(int(n * (n+1)/2))

sum_nums(100)