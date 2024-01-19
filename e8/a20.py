s = input()
t = input()

dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]

for i in range(1, len(dp)):
  for j in range(1, len(dp[i])):
    if t[i - 1] == s[j - 1]:
      dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1] + 1)
    else:
      dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])


def array_print(arr):
  for v in arr:
    print(v)

# array_print(dp)
print(dp[-1][-1])
