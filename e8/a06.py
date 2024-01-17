N, Q = map(int, input().split())
a = list(map(int, input().split()))
arr = [0]
for i in range(N):
  arr.append(arr[-1] + a[i])

for _ in range(Q):
  l, r = map(int,input().split())
  print(arr[r] - arr[l - 1])