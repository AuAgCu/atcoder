N, K = map(int, input().split())
a = list(map(int, input().split()))

t = 0
e = 10 ** 9

for i in range(100):
  m = (e + t) // 2

  count = 0
  for v in a:
    count += m // v

  print(t, m, e, count)
  if count == K:
    print(m)
    exit()
  elif count < K:
    if t == m:
      t = e
    else:
      t = m
  else:
    if e == m:
      e = m
    else:
      e = m
