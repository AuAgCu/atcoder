N = int(input())
a = list(map(int, input().split()))

ans = [[False for _ in range(3)] for _ in range(N)]

for i in range(N):
  for j in range(1, 3):
    ans[i][j] = not ans[i][0]

  if i + 1 < N:
    ans[i + 1][0] = not ans[i][0]

def pr(arr):
  for v in arr:
    print(v)

pr(ans)