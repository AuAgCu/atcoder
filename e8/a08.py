def print_arr(arr):
  for v in arr:
    print(v)

H, W = map(int, input().split())
xs = []
for i in range(H):
  x = list(map(int, input().split()))
  xs.append(x)

arrs = [[0] * (W+1)]
for v in xs:
  arr = [0]
  for w in v:
    arr.append(arr[-1] + w)

  arrs.append(arr)

for i in range(1, len(arrs)):
  for j in range(len(arrs[i])):
    arrs[i][j] += arrs[i-1][j]

Q = int(input())
for i in range(Q):
  a, b, c, d = map(int, input().split())
  t1 = arrs[c][d] - arrs[a-1][d]
  t2 = arrs[c][b-1] - arrs[a-1][b-1]
  print(t1 - t2)
  