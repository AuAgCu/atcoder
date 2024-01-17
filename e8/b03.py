N = int(input())
a = list(map(int, input().split()))

for i in range(N):
  for j in range(i + 1, N):
    for k in range(j + 1, N):
      if a[i] + a[j] + a[k] == 1000:
        print('Yes')
        exit()

print('No')
