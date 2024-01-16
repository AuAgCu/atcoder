import bisect

N, K = map(int, input().split())
a = list(map(int, input().split()))

count = 0
for i in range(len(a)):
  v = a[i]
  index = bisect.bisect_right(a, v + K)
  count += index - i - 1

print(count)