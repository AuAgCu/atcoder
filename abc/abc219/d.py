import sys

N = int(input())
X,Y = map(int, input().split())

dp = [[sys.maxsize for _ in range(Y+1)] for _ in range(X+1)]
dp[0][0] = 0

array = []
for _ in range(N):
    a, b = map(int, input().split())
    array.append((a, b))

for i in range(N):
    a, b = array[i]
    for j in reversed(range(len(dp))):
        for k in reversed(range(len(dp[j]))):
            tmp_j = min(X, a+j)
            tmp_k = min(Y, b+k)
            dp[tmp_j][tmp_k] = min(dp[tmp_j][tmp_k], dp[j][k]+1)

if dp[X][Y] == sys.maxsize:
    print(-1)
else:
    print(dp[X][Y])
