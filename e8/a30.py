def kaijou(n):
  ans = 1
  for i in range(1, n + 1):
    ans *= i
    ans %= MOD

  return ans

MOD = 1000000007 
n, r = map(int, input().split())

i = 1
ue = kaijou(n)

sita = kaijou(r) * kaijou(n - r)
sita %= MOD

ans = ue * pow(sita, MOD - 2, MOD)

print(ans % MOD)