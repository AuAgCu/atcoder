A, B = map(int, input().split())

if A < B:
  A, B = B, A

while A % B != 0:
  A = A % B

  A, B = B, A

print(B)