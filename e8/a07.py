D = int(input())
N = int(input())
arr = [0] * (D + 2)

for i in range(N):
  l, r = map(int, input().split())
  arr[l] += 1
  arr[r + 1] -= 1

count = 0
for i in range(1, D + 1):
  count += arr[i]
  print(count)
  