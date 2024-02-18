MOD = 10 ** 9 + 7

count = 0
ans = 1
a, b = map(int, input().split())

dic = {
  1: a
}

i = 1
while i <= b:
  dic[i * 2] = dic[i] ** 2
  dic[i * 2] %= MOD

  i *= 2

keys = list(reversed(sorted(dic.keys())))
# print(list(keys))
ans = 1
while b != 0:
  for key in keys:
    if b >= key:
      ans *= dic[key]
      ans %= MOD
      b -= key
      break

print(ans)
    