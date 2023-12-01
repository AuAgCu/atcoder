N, K = map(int, input().split())

n = N
for _ in range(K):
    if n % 200 == 0:
        n //= 200
    else:
        n = n * 1000 + 200

print(n)