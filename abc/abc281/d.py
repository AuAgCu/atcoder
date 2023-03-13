N, K, D = map(int, input().split())

a = list(map(int, input().split()))
dp = [[-1 for _ in range(D)] for _ in range(K + 1)]
dp[0][0] = 0

for i in range(N):
    v = a[i]
    for j in reversed(range(len(dp) - 1)):
        for k in range(len(dp[j])):
            w = dp[j][k]
            if w == -1:
                continue
            tmp = w + v
            key = tmp % D
            dp[j+1][key] = max(dp[j+1][key], tmp)

print(dp[-1][0])


