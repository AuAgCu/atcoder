N, M, B = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

ans_c = sum(c)

ans = 0
for i in range(N):
  ans += (a[i] + B) * M + ans_c

print(ans)