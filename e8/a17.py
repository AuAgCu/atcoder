N = int(input())
a = [None, None]
a.extend(list(map(int, input().split())))
b = [None, None, None]
b.extend(list(map(int, input().split())))

dp = [0] * (N + 1)
dp[2] = a[2]
for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + a[i], dp[i - 2] + b[i])

d = [N]
while d[-1] != 1:
    now = d[-1]
    v = dp[now]

    if dp[now - 1] + a[now] == v:
        d.append(now - 1)
    else:
        d.append(now - 2)

ans = reversed(list(map(str, d)))
print(len(d))
print(' '.join(ans))