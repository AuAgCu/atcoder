N, K = map(int, input().split())
print(sum([i * 100 * K for i in range(1, N + 1)]) + N * sum([j for j in range(1, K + 1)]))

ans = 0
for i in range(1, N + 1):
    for j in range(1, K + 1):
        ans += i * 100 + j

print(ans)