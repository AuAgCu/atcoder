N, X, Y = map(int, input().split())

a = list(map(int, input().split()))


M = 100000
array = [-1] * (M + 1) 
for i in range(M):
  arr_X = [False] * 3
  if i < X and i < Y:
    pass
  elif i < Y:
    if array[i - X] < 3:
      arr_X[array[i - X]] = True
  else:
    if array[i - X] < 3:
      arr_X[array[i - X]] = True
    if array[i - Y] < 3:
      arr_X[array[i - Y]] = True

  if not arr_X[0]:
    array[i] = 0
  elif arr_X[1]:
    array[i] = 2
  else:
    array[i] = 1

grundy = []
for i in range(N):
  grundy.append(array[a[i]])

first = grundy[0]
for i in range(1, N):
  first ^= grundy[i]

if first == 0:
  print('Second')
else:
  print('First')
