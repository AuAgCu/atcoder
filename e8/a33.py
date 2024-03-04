N = int(input())

a = list(map(int, input().split()))

first = a[0]
for i in range(1, N):
  first ^= a[i]

if first == 0:
  print('Second')
else:
  print('First')