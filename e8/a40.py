import math
N = int(input())
a = list(map(int, input().split()))

dic = {}
for v in a:
  dic.setdefault(v, 0)
  dic[v] += 1

ans = 0
for v in dic.values():
  if v < 3:
    continue

  ans += math.comb(v, 3)

print(ans)