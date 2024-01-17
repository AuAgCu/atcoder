N = int(input())
a = list(map(int, input().split()))

t = 1
e = ((N if N % 2 != 0 else N - 1) + 1) // 2
m = (e + t) // 2 

count = 0
while t < e:
  count += 1
  m = (e + t) // 2 + 1

  success = False
  for i in range(N - (m * 2 - 1) + 1):
    ts = True
    for j in range(m * 2 - 1):
        
      if (m * 2 - 1) // 2 + 1 > j:
        if a[i + j] < j + 1:
          ts = False
      else:
        if a[i + j] < (m * 2 - 1) - j:
          ts = False

    if ts:
      success = True
  

  if success:
    t = m
  else:
    e = m - 1

print(t)