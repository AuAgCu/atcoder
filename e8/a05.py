N, K = map(int, input().split())
count = 0
for i in range(1, N + 1):
  for j in range(1, N + 1):
    if i + j >= K:
      continue

    if K - i - j > N:
      continue
    
    count += 1

print(count)
