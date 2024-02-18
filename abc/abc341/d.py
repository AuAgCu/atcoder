import math, sys, time
N, M, K = map(int, input().split())

koubai = N * M // math.gcd(N, M)

l = 1
r = sys.maxsize
while True:
  m = (l + r) // 2
  a = m // koubai
  b = m // N - a
  c = m // M - a

  if c + b == K and ((m % N == 0 or m % M == 0) and m % koubai != 0):
    print(m)
    exit(0)

  if b + c >= K:
    r = m
  else:
    l = m
