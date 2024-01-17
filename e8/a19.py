def array_print(arr):
    for v in arr:
        print(v)

N, W = map(int, input().split())

wv = []
for i in range(N):
    w, v = map(int, input().split())
    wv.append((w, v))

dp = [[0 for _ in range(W + 1)] for _ in range(N)]

if wv[0][0] <= W:
    dp[0][wv[0][0]] = wv[0][1]

for i in range(1, N):
    for j in range(W + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j])
        w, v = wv[i]
        nextW = j + w
        if nextW <= W:
            dp[i][nextW] = max(dp[i][nextW], dp[i - 1][j] + v)
            
print(max(dp[-1]))
