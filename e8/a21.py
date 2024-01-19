N = int(input())

pa = []
for _ in range(N):
    p, a = map(int, input().split())
    pa.append((p, a))

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        left = i 
        right = N - j - 1

        pl, al = pa[left]
        if left + 1 <= pl and pl <= right + 1:
            lv = dp[i][j] + al
        else:
            lv = dp[i][j]

        dp[i + 1][j] = max(dp[i + 1][j], lv)

        pr, ar = pa[right]
        if left + 1 <= pr and pr <= right + 1:
            rv = dp[i][j] + ar
        else:
            rv = dp[i][j]

        dp[i][j + 1] = max(dp[i][j + 1], rv)

def arr_print(arr):
    for v in arr:
        print(v)

# arr_print(dp)
ans = 0
for i in range(N):
    j = N - i
    ans = max(ans, dp[i][j])

print(ans)