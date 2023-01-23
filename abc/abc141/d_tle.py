N, M = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(M):
    a = sorted(a, reverse=True)
    a[0] //= 2
    
print(sum(a))