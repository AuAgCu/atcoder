a = [0, 2, 4, 6, 8]
n = int(input()) - 1

if n == 0:
  print(0)

ans = []

while n != 0:
  ans.append(str(a[n%5]))
  n //= 5

ans.reverse()
print(''.join(ans))