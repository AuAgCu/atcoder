N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False for _ in range(N)] for _ in range(S + 1)]
dp[0][0] = True

if A[0] <= S:
    dp[A[0]][0] = True
for i in range(1, N):
    for j in range(S + 1):
        if dp[j][i - 1]:
            dp[j][i] = True

            if j + A[i] <= S:
                dp[j + A[i]][i] = True

print('Yes' if dp[-1][-1] else 'No')

