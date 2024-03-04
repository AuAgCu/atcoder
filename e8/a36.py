N, K = map(int, input().split())

if K >= (N-1) * 2 and K % 2 == 0:
  print('Yes')
else:
  print('No')