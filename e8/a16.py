N = int(input())
a = [None, None]
a.extend(list(map(int, input().split())))
b = [None, None, None]
b.extend(list(map(int, input().split())))

dp = [0] * (N + 1)
dp[2] = a[2]
for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + a[i], dp[i - 2] + b[i])

# print(dp)
print(dp[-1])