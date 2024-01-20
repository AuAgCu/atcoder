import bisect

N = int(input())
a = list(map(int, input().split()))

dp = [0] * (N + 1)
l = [0]
for i in range(N):
  index = bisect.bisect(l, a[i] - 1)

  next_count = index
  dp[i + 1] = next_count

  if next_count < len(l):
    l[next_count] = min(a[i], l[next_count])
  else:
    l.append(a[i])

# print(dp)
# print(l)
print(max(dp))

  
