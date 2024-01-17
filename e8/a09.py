def array_print(arr):
  for v in arr:
    print(v)

  print()

H, W, N = map(int, input().split())

arrs = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
for i in range(N):
  a, b, c, d = map(int, input().split())
  a -= 1
  b -= 1

  arrs[a][b] += 1
  arrs[c][b] -= 1
  arrs[a][d] -= 1
  arrs[c][d] += 1

for i in range(len(arrs)):
  for j in range(1, len(arrs[i])):
    arrs[i][j] += arrs[i][j-1]

for i in range(1, len(arrs)):
  for j in range(len(arrs[i])):
    arrs[i][j] += arrs[i-1][j]

for v in arrs[:-1]:
  print(' '.join(map(str, v[:-1])))
