N = int(input())

arr = []
while N != 0:
  arr.append(str(N % 2))
  N //= 2

while len(arr) != 10:
  arr.append('0')

print(''.join(reversed(arr)))
