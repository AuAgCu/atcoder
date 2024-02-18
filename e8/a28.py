N = int(input())

ans = 0
for i in range(N):
  T, A = input().split()
  if T == '+':
    ans += int(A)
  elif T == '-':
    ans -= int(A)
  else:
    ans *= int(A)

  ans %= 10000

  print(ans)