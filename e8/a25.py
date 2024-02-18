H, W = map(int, input().split())

arr = []
for i in range(H):
  arr.append(input())

dp = [[0 for _ in range(H + 1)] for _ in range(W + 1)]
dp[0][1] = 1
for i in range(1, W + 1):
  for j in range(1, H + 1):
    if arr[j-1][i-1] == '#':
      continue

    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]


def ap(arr):
  for v in arr:
    print(v)

print(dp[-1][-1])