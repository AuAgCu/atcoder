N, K = map(int, input().split())
a = list(map(int, input().split()))

t = 0
e = 10 ** 9

while t != e:
  m = (e + t) // 2

  count = 0
  for v in a:
    count += m // v

  # print(t, m, e, count)
  if count < K:
    t = m + 1
  else:
    e = m

print(e)