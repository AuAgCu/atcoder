N, M = map(int, input().split())
dp = [[100 for _ in range(2 ** N)] for _ in range(M + 1)]
dp[0][0] = 0

A = []
for i in range(M):
    a = list(reversed(input().split()))
    a = int(''.join(a), 2)
    A.append(a)

for i in range(M):
    a = A[i]

    for j in range(len(dp[i])):
        dp[i + 1][j] = min(dp[i][j], dp[i+1][j])
        index = a | j
        dp[i + 1][index] = min(dp[i][j] + 1, dp[i + 1][index])

def arr_print(arr):
    for v in arr:
        print(v)

if dp[-1][-1] >= 100:
    print(-1)
else:
    print(dp[-1][-1])