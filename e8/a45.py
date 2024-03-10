N, C = input().split()
N = int(N)
a = input()

w, b, r = 0, 0, 0
for c in a:
  if c == 'B':
    b += 1
  elif c == 'R':
    r += 1
  else:
    w += 1

result = ''
if (b - r) % 3 == 0:
  result = 'W'
elif (b - r) % 3 == 1:
  result = 'B'
else:
  result = 'R'

print('Yes' if result == C else 'No')