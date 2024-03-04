N = int(input())
S = input()
Q = int(input())

arr = [chr(i) for i in range(97, 123)]

for i in range(Q):
  c, d = input().split()
  oc, od = ord(c) - 97, ord(d) - 97

  for j in range(len(arr)):
    if arr[j] == c:
      arr[j] = d

for s in S:
  print(arr[ord(s) - 97], end='')

print()