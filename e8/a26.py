import math
Q = int(input())

for i in range(Q):
  x = int(input())

  flag = True
  for j in range(2, math.floor(math.sqrt(x)) + 1):
    if x % j == 0:
      flag = False
      print('No')
      break

  if flag:
    print('Yes')

