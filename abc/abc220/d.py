MOD = 998244353

N = int(input())
array = list(map(int, input().split()))
ans = [[0 for _ in range(10)] for _ in range(N)]

ans[0][array[0]] = 1
for i in range(1, N):
    for j in range(10):
        ans[i-1][j] %= MOD
        plus = (j + array[i]) % 10
        multi = (j * array[i]) % 10
        ans[i][plus] += ans[i-1][j]
        ans[i][multi] += ans[i-1][j]

for v in ans[-1]:
    print(v % MOD)