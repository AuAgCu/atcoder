import sys

N, K = map(int, input().split())    
ab = []
for i in range(N):
    a, b = map(int, input().split())
    ab.append((a, b))

ab.sort(reverse=True)

ans = 0
k = K
while k != 0:
    ans += k
    k = 0
    while len(ab) != 0 and ab[-1][0] <= ans:
        _, b = ab.pop()
        k += b

print(ans)