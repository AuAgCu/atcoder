N = int(input())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

dp = [-1] * N
dp[0] = 0
for i in range(N - 1):
    if dp[i] == -1:
        continue

    a = a_arr[i]
    b = b_arr[i]

    dp[a - 1] = max(dp[a - 1], dp[i] + 100)
    dp[b - 1] = max(dp[b - 1], dp[i] + 150)

print(dp[-1])