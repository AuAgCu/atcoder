import sys

N, L = map(int, input().split())
ans = 0
for i in range(N):
  aa, b = input().split()
  a = int(aa)

  ans = max(ans, a if b == 'W' else (L - a))

print(ans)